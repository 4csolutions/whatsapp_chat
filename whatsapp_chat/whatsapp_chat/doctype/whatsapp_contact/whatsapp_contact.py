# Copyright (c) 2024, shridhar patil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WhatsAppContact(Document):

	def after_insert(self):
		payload = {
			"room": self.name,
			"room_name": self.contact_name,
			"user_email": self.mobile_no,
			"opposite_person_email": self.mobile_no,
			"last_message": self.last_message,
			"last_date": frappe.utils.str_utc(self.modified) if self.modified else frappe.utils.now(),
			"is_read": self.is_read,
			"email": self.email
		}
		if self.email:
			frappe.publish_realtime(
				"new_room_creation", 
				payload, 
				user=self.email
			)
		else:
			frappe.publish_realtime(
				"new_room_creation", 
				payload
			)

	pass
