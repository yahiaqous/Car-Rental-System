from odoo import models, fields, api
from odoo.exceptions import UserError


class Car(models.Model):
    _name = 'car_rental_system.car'
    _description = 'car_rental_system.car'

    active = fields.Boolean(default=True)

    name = fields.Char('Car Name', required=True)
    description = fields.Text('Brief Description')
    rent_price = fields.Float('Rent Price', required=True)
    state = fields.Selection(
        [('available', 'Available'),
         ('rented', 'Rented'),
         ('damaged', 'Damaged')],
        'State', default="available")

    # Methods

    def change_state(self, new_state):
        for car in self:
            car.state = new_state

    def mark_available(self):
        self.active = True
        self.change_state('available')

    def mark_reserved(self):
        self.active = True
        self.change_state('rented')

    def mark_damaged(self):
        self.active = False
        self.change_state('damaged')

    def reserve_car(self):
        self.ensure_one()
        if self.state != 'available':
            raise UserError(('Car is not available for renting'))

        # Manager => Open the Reservation Wizard View
        if self.env.user.has_group('car_rental_system.group_managers'):
            return self.open_reservation_wizard_action_view()

        # User => Reserve Direct
        else:
            self.env['car_rental_system.car_reservation'].sudo().create({
                'car_id': self.id,
                'borrower_id': self.env.user.partner_id.id,
            })

        self.sudo().mark_reserved()

    @api.model
    def open_reservation_wizard_action_view(self):
        action = self.env.ref(
            'car_rental_system.action_wizard_rent_cars').read()[0]
        action['context'] = {'car_ids': self.id}
        return action

    def unreserve_car(self):
        self.ensure_one()
        if self.state != 'rented':
            raise UserError(('Car is not reserved yet'))

        reserved_car = self.env['car_rental_system.car_reservation'].sudo().search(
            [('car_id', '=', self.id), ('return_date', '=', None)])
        # Save the Return Date => Now
        reserved_car.return_date = fields.Datetime.now()
        reserved_car.reservation_state = 'returned'

        self.mark_available()

    def damaged_car(self):
        self.ensure_one()
        if self.state == 'damaged':
            raise UserError(('Car is already damaged'))

        reserved_car = self.env['car_rental_system.car_reservation'].sudo().search(
            [('car_id', '=', self.id), ('return_date', '=', None)])
        # Save the Return Date => Now
        reserved_car.return_date = fields.Datetime.now()
        reserved_car.reservation_state = 'returned'

        self.mark_damaged()
