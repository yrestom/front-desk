# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "inn"
app_title = "Inn Hotels"
app_publisher = "Core Initiative"
app_description = "Apps for handling hotel business"
app_icon = "octicon octicon-book"
app_color = "blue"
app_email = "info@coreinitiative.id"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/inn/css/inn.css"
# app_include_js = "/assets/inn/js/inn.js"

# include js, css files in header of web template
# web_include_css = "/assets/inn/css/inn.css"
# web_include_js = "/assets/inn/js/inn.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "inn.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "inn.install.before_install"
# after_install = "inn.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "inn.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# 	"*": {
	# 		"on_update": "method",
	# 		"on_cancel": "method",
	# 		"on_trash": "method"
	#	}
	"Inn Tax": {
		"validate": "inn.inn.doctype.inn_tax.inn_tax.autofill_inn_tax_value"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"inn.tasks.all"
# 	],
# 	"daily": [
# 		"inn.tasks.daily"
# 	],
# 	"hourly": [
# 		"inn.tasks.hourly"
# 	],
# 	"weekly": [
# 		"inn.tasks.weekly"
# 	]
# 	"monthly": [
# 		"inn.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "inn.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "inn.event.get_events"
# }
