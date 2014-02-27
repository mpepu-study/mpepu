from edc.subject.registration.models.registered_subject import RegisteredSubject
from datetime import date, timedelta


class NonRandomizedInfants(object):

    def __init__(self, site=None, search_date=date.today(), cutoff=34, earliest=14):
        self.search_date = search_date
        self.site = site
        self.cutoff = cutoff
        self.earliest = earliest
        self.eligibles = self.eligible_search()

    def eligible_search(self, search_date=date.today(), cutoff=34, earliest=14):
        old_dob = search_date - timedelta(days=cutoff)
        recent_dob = search_date - timedelta(days=earliest)
        eligibles = RegisteredSubject.objects.select_related('studysite').filter(
            subject_type__iexact='infant',
            registration_status__iexact='registered',
            dob__range=[old_dob, recent_dob],
        )
        if self.site:
            eligibles = eligibles.filter(study_site__site_name__iexact=self.site)
        else:
            eligibles = eligibles.order_by('study_site__site_name')
        self.eligible_count = eligibles.count()
        eligible_infants = (self.wrap_registered_subject(subject) for subject in eligibles)
        return eligible_infants

    def wrap_registered_subject(self, registered_subject):
        class EligibleInfant(object):
            def __init__(self, registered_subject, earliest, cutoff, search_date=date.today()):
                self.infant = registered_subject
                self.cutoff = cutoff
                self.earliest = earliest
                self.search_date = search_date

            def days_from_early_date(self):
                diff = self.search_date - self.infant.dob - timedelta(days=self.earliest)
                return diff.days

            def days_from_expiration(self):
                diff = timedelta(days=self.cutoff) - (self.search_date - self.infant.dob)
                return diff.days

            def age(self):
                diff = self.search_date - self.infant.dob
                return diff.days

        return EligibleInfant(registered_subject, self.earliest, self.cutoff, self.search_date)