from odoo import models, fields, api


class CarReserveWizard(models.TransientModel):
    _name = 'crs.car_reservation.wizard'

    borrower_id = fields.Many2one(
        'res.partner', string='Borrower', required=True, default=lambda self: self.env.user.partner_id)
    car_ids = fields.Many2many(
        'car_rental_system.car', string='Cars', required=True)

    def add_car_reservation(self):
        self.ensure_one()
        rentModel = self.env['car_rental_system.car_reservation'].sudo()
        for car in self.car_ids:
            newRent = rentModel.create({
                'borrower_id': self.borrower_id.id,
                'car_id': car.id
            })

            newRent.car_id.mark_reserved()

        return {
            # Rainbow Man Effect
            'effect': {
                'fadeout': 'slow',
                'message': 'Car Rent Successfully by %s' % (self.borrower_id.display_name),
                'type': 'rainbow_man',
            }
        }

    @api.model
    def default_get(self, fields_list):
        defaults = super(CarReserveWizard, self).default_get(fields_list)
        if self.env.context.get('active_model'):
            defaults['car_ids'] = [self.env.context['car_ids']]
        return defaults
