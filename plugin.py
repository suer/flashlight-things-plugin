#!/usr/bin/python
# -*- coding: utf-8 -*-

def results(parsed, original_query):
    return {
        'title': 'Add task to Things',
        'run_args': [parsed['~task']]
    }

def run(task):
    from Foundation import *
    from ScriptingBridge import *
    things = SBApplication.applicationWithBundleIdentifier_('com.culturedcode.things')
    things.showQuickEntryPanelWithAutofill_withProperties_(False, { 'name' : unicode(task.encode('utf-8'), encoding='utf-8') })
