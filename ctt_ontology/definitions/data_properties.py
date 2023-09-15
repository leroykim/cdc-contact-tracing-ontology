import datetime
from owlready2 import get_ontology, DataProperty
from ctt_ontology.util.config import Configuration
from ctt_ontology.definitions.classes import *

ctt_ontology = get_ontology(Configuration.namespace)

with ctt_ontology:
    # Patient data properties
    class date_assigned_to_investigation(DataProperty):
        domain = [Patient]
        range = [datetime.date]

    class patient_id(DataProperty):
        domain = [Patient]
        range = [str]

    # ContactTracing data properties
    class any_household_contact(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class total_number_of_household_contacts(DataProperty):
        domain = [ContactTracing]
        range = [int]

    class can_self_isolate(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class need_assistance_to_self_isolate(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class any_intimate_partners(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class total_number_of_intimate_partners(DataProperty):
        domain = [ContactTracing]
        range = [int]

    class any_other_close_contact(DataProperty):
        domain = [ContactTracing]
        range = [str]

    # Interview data properties
    class interview_1_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class interview_2_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class interview_3_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class date_of_interview_attempt_1(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    class date_of_interview_attempt_2(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    class date_of_interview_attempt_3(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    # LocatingInformation data properties
