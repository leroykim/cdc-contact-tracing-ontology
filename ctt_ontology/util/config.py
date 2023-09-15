import yaml
from dataclasses import dataclass

with open("configuration.yaml", "r") as configuration_file:
    configuration = yaml.safe_load(configuration_file)


@dataclass
class Configuration:
    with open("configuration.yaml", "r") as configuration_file:
        __configuration = yaml.safe_load(configuration_file)

    namespace = __configuration["namespace"]

    date_format = __configuration["date_format"]
    start_date = __configuration["start_date"]
    end_date = __configuration["end_date"]

    YNUR = __configuration["YNUR"]
    YNPR = __configuration["YNPR"]
    PNUE = __configuration["PNUE"]
    YN = __configuration["YN"]
    CONGREGATE = __configuration["CONGREGATE"]
    EMPLOYED = __configuration["EMPLOYED"]
    HCP = __configuration["HCP"]
    CONTACT = __configuration["CONTACT"]
    ETHNICITY = __configuration["ETHNICITY"]
    GENDER = __configuration["GENDER"]
    LANGUAGE = __configuration["LANGUAGE"]
    RACE = __configuration["RACE"]
