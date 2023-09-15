from abc import ABC, abstractmethod
import datetime
import random
import uuid

from ctt_ontology.util.config import Configuration
from ctt_ontology.definitions.classes import *
from ctt_ontology.definitions.data_properties import *


class ClassGenerator(ABC):
    def __init__(self):
        self.start_date = datetime.datetime.strptime(
            Configuration.start_date, Configuration.date_format
        )
        self.end_date = datetime.datetime.strptime(
            Configuration.end_date, Configuration.date_format
        )

    @abstractmethod
    def generate(self):
        pass

    def get_random_date(self) -> datetime.date:
        delta = self.end_date - self.start_date
        random_number_of_days = random.randint(0, delta.days)
        random_date = self.start_date + datetime.timedelta(days=random_number_of_days)
        return random_date.date()


class PatientGenerator(ClassGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        patient = Patient()
        patient.date_assigned_to_investigation.append(self.get_random_date())
        patient.patient_id.append(str(uuid.uuid4()))
        return patient


class ContactTracingGenerator(ClassGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        contact_tracing = ContactTracing()
        household_contact = random.choice(Configuration.YNUR)
        contact_tracing.any_household_contact.append(household_contact)
        if household_contact == "Y":
            contact_tracing.total_number_of_household_contacts.append(
                random.randint(0, 10)
            )
        else:
            contact_tracing.total_number_of_household_contacts.append(0)
        contact_tracing.can_self_isolate.append(random.choice(Configuration.YNUR))
        contact_tracing.need_assistance_to_self_isolate.append(
            random.choice(Configuration.YNUR)
        )
        intimate_partners = random.choice(Configuration.YNUR)
        contact_tracing.any_intimate_partners.append(intimate_partners)
        if intimate_partners == "Y":
            contact_tracing.total_number_of_intimate_partners.append(
                random.randint(0, 10)
            )
        else:
            contact_tracing.total_number_of_intimate_partners.append(0)
        contact_tracing.any_other_close_contact.append(
            random.choice(Configuration.YNUR)
        )
        return contact_tracing


class InterviewGenerator(ClassGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        interview = Interview()
        interview.interview_1_occurred.append(random.choice(Configuration.YNPR))
        interview.interview_2_occurred.append(random.choice(Configuration.YNPR))
        interview.interview_3_occurred.append(random.choice(Configuration.YNPR))
        interview.date_of_interview_attempt_1.append(self.get_random_date())
        interview.date_of_interview_attempt_2.append(self.get_random_date())
        interview.date_of_interview_attempt_3.append(self.get_random_date())

        return interview
