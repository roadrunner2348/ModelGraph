from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
from django.template import loader, Context
from django.db.models import Count
from server.models import *
from django.shortcuts import get_object_or_404
import server.utils as utils

class ModelGraph(IPlugin):
	def show_widget(self, page, machines=None, theid=None):

		if page == 'front':
			t = loader.get_template('justinwolf/modelgraph/templates/front.html')
			if not machines:
				machines = Machine.objects.all()

		if page == 'bu_dashboard':
			t = loader.get_template('justinwolf/modelgraph/templates/id.html')
			if not machines:
				machines = utils.getBUmachines(theid)

		if page == 'group_dashboard':
			t = loader.get_template('justinwolf/modelgraph/templates/id.html')
			if not machines:
				machine_group = get_object_or_404(MachineGroup, pk=theid)
				machines = Machine.objects.filter(machine_group=machine_group)

		if machines:
			model_info = machines.values('machine_model').annotate(count=Count('machine_model')).order_by()
		else:
			munki_info[]


		c = Context({
			'title': 'Model Breakdown',
			'data': munki_info,
			'page': page,
			'theid': theid
			})
		return t.render(c), 3