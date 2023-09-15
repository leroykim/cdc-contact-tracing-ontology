from owlready2 import get_ontology, Thing
from ctt_ontology.util.config import Configuration

ctt = get_ontology(Configuration.namespace)

with ctt:

    class ContactTracing(Thing):
        pass

    class Interview(Thing):
        pass

    class LocatingInformation(Thing):
        pass

    class Patient(Thing):
        pass

    class PreExistingConditions(Thing):
        pass

    class RiskFactors(Thing):
        pass

    class SARSCOV2Test(Thing):
        pass

    class SymptomsAndClinicalCourse(Thing):
        pass
