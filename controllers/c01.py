# -*- coding: utf-8 -*-

def home():
	form = FORM(
		INPUT(
			_type = "submit",
			_value = "Submit",
			)
		)
	if (form.process().accepted):
		redirect(
			URL(
				a = "redirect",
				c = "c01",
				f = "page_two",
				)
			)
	return dict(
		form = form,
		)
def page_two():
	message = "You are on page two!!!"
	home = A(
		"home",
		_href = URL(
			a = "redirect",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		message = message,
		)
