from odoo import models, fields, api


class CarReservation(models.Model):
    _name = 'car_rental_system.car_reservation'
    _description = 'car_rental_system.car_reservation'

    car_id = fields.Many2one("car_rental_system.car",
                             string="Car", required=True, ondelete='cascade')
    borrower_id = fields.Many2one(
        "res.partner", string="Borrower", required=True)
    reservation_state = fields.Selection(
        [('ongoing', 'Ongoing'),
         ('return_request', 'Return Request'),
         ('returned', 'Returned')],
        'Reservation State', default="ongoing")

    return_date = fields.Datetime(string="Return Date")

    def unreserve_car(self):
        self.car_id.sudo().unreserve_car()

    def request_unreserve_car(self):
        self.sudo().reservation_state = 'return_request'
