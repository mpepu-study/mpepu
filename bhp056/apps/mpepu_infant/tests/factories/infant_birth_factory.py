import factory
from datetime import date
from edc.base.model.tests.factories import BaseUuidModelFactory
from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from ..tests.factories import MaternalLabDelFactory
from mpepu_infant.models import InfantBirth


class InfantBirthFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantBirth

    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    maternal_lab_del = factory.SubFactory(MaternalLabDelFactory)
    first_name = factory.Sequence(lambda n: 'ERIK{0}'.format(n))
    initials = factory.Sequence(lambda n: 'E{0}V'.format(n))
    dob = date.today()
    gender = 'M'