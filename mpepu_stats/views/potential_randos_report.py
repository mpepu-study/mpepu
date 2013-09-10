from datetime import datetime, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mpepu_infant.models import InfantBirth


@login_required
def potential_randos_report(request, **kwargs):

    section_name = kwargs.get('section_name')
    report_title = 'Potential vs Missed Randomizations'
    template = 'potential_randos_report.html'

    # get all births / infants
    infantbirth_aggregates = InfantBirth.objects.all().aggregate(Count('dob'), Avg('dob'), Max('dob'), Min('dob'), StdDev('dob'), Variance('dob'))
    cutoff_dob = datetime.today() - timedelta(34)

    missed_randos = InfantBirth.objects.filter(dob__lt=cutoff_dob, registered_subject__sid__isnull=True).order_by('dob')
    potential_randos = InfantBirth.objects.filter(dob__gte=cutoff_dob, registered_subject__sid__isnull=True).order_by('dob')

    return render_to_response(template, {
        'infantbirth_aggregates': infantbirth_aggregates,
        'missed_randos': missed_randos,
        'potential_randos': potential_randos,
        'cutoff_dob': cutoff_dob,
        'section_name': section_name,
        'report_title': report_title,
        'report': '',
        'report_name': kwargs.get('report_name'),
        }, context_instance=RequestContext(request))