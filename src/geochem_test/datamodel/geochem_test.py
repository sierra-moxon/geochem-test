# Auto generated from geochem_test.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-13T16:24:50
# Schema: geochem-test
#
# id: https://w3id.org/sierra-moxon/geochem-test
# description: A geochemical microschema for modeling well-field experiment observations,
#   designed to conform to bertron-schema's Entity pattern using named slots
#   instead of a generic properties bag.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Decimal, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URI, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
UCUM = CurieNamespace('UCUM', 'https://units-of-measurement.org/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BERTRON = CurieNamespace('bertron', 'https://w3id.org/bertron-schema/')
COMS = CurieNamespace('coms', 'https://w3id.org/linkml/linkml-microschema-profile/')
GEOCHEM_TEST = CurieNamespace('geochem_test', 'https://w3id.org/sierra-moxon/geochem-test/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = GEOCHEM_TEST


# Types

# Class references
class GeochemDatasetId(URIorCURIE):
    pass


@dataclass(repr=False)
class Quantity(YAMLRoot):
    """
    A numeric value with an optional unit. Designed for inline composition (no identifier). Compatible with bertron's
    QuantityValue.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["QuantitativeValue"]
    class_class_curie: ClassVar[str] = "schema:QuantitativeValue"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.Quantity

    quantity_value: Decimal = None
    quantity_unit: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        if self.quantity_unit is not None and not isinstance(self.quantity_unit, URIorCURIE):
            self.quantity_unit = URIorCURIE(self.quantity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TracerExperimentMetadata(YAMLRoot):
    """
    Metadata for a tracer experiment, including initial concentrations and flow rate extracted from the spreadsheet
    header.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["TracerExperimentMetadata"]
    class_class_curie: ClassVar[str] = "geochem_test:TracerExperimentMetadata"
    class_name: ClassVar[str] = "TracerExperimentMetadata"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.TracerExperimentMetadata

    initial_iodine_concentration: Optional[Union[dict, Quantity]] = None
    initial_cesium_concentration: Optional[Union[dict, Quantity]] = None
    flow_rate: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.initial_iodine_concentration is not None and not isinstance(self.initial_iodine_concentration, Quantity):
            self.initial_iodine_concentration = Quantity(**as_dict(self.initial_iodine_concentration))

        if self.initial_cesium_concentration is not None and not isinstance(self.initial_cesium_concentration, Quantity):
            self.initial_cesium_concentration = Quantity(**as_dict(self.initial_cesium_concentration))

        if self.flow_rate is not None and not isinstance(self.flow_rate, Quantity):
            self.flow_rate = Quantity(**as_dict(self.flow_rate))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeochemObservation(YAMLRoot):
    """
    A single geochemical measurement observation. Replaces bertron's generic properties bag with named slots for
    measurement data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["GeochemObservation"]
    class_class_curie: ClassVar[str] = "geochem_test:GeochemObservation"
    class_name: ClassVar[str] = "GeochemObservation"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.GeochemObservation

    measurement_type: Union[str, "GeochemMeasurementTypeEnum"] = None
    measurement_value: Union[dict, Quantity] = None
    sample_name: Optional[str] = None
    uncertainty: Optional[Union[dict, Quantity]] = None
    time_since_start: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, GeochemMeasurementTypeEnum):
            self.measurement_type = GeochemMeasurementTypeEnum(self.measurement_type)

        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, Quantity):
            self.measurement_value = Quantity(**as_dict(self.measurement_value))

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.uncertainty is not None and not isinstance(self.uncertainty, Quantity):
            self.uncertainty = Quantity(**as_dict(self.uncertainty))

        if self.time_since_start is not None and not isinstance(self.time_since_start, Quantity):
            self.time_since_start = Quantity(**as_dict(self.time_since_start))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RadonObservation(GeochemObservation):
    """
    A radon-222 activity concentration measurement. Expected measurement_type: radon_222, unit: pCi/L.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["RadonObservation"]
    class_class_curie: ClassVar[str] = "geochem_test:RadonObservation"
    class_name: ClassVar[str] = "RadonObservation"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.RadonObservation

    measurement_type: Union[str, "GeochemMeasurementTypeEnum"] = None
    measurement_value: Union[dict, Quantity] = None

@dataclass(repr=False)
class TracerConcentrationObservation(GeochemObservation):
    """
    A tracer concentration measurement (iodine or cesium). Expected unit: ppb (iodine) or ppm (cesium).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["TracerConcentrationObservation"]
    class_class_curie: ClassVar[str] = "geochem_test:TracerConcentrationObservation"
    class_name: ClassVar[str] = "TracerConcentrationObservation"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.TracerConcentrationObservation

    measurement_type: Union[str, "GeochemMeasurementTypeEnum"] = None
    measurement_value: Union[dict, Quantity] = None

@dataclass(repr=False)
class WaterQualityObservation(GeochemObservation):
    """
    A water quality parameter measurement (temperature, dissolved oxygen, specific conductance, pH, or ORP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["WaterQualityObservation"]
    class_class_curie: ClassVar[str] = "geochem_test:WaterQualityObservation"
    class_name: ClassVar[str] = "WaterQualityObservation"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.WaterQualityObservation

    measurement_type: Union[str, "GeochemMeasurementTypeEnum"] = None
    measurement_value: Union[dict, Quantity] = None

@dataclass(repr=False)
class GeochemDataset(YAMLRoot):
    """
    A dataset containing geochemical observations from a well-field experiment. Serves as the tree root and mirrors
    bertron Entity core slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_TEST["GeochemDataset"]
    class_class_curie: ClassVar[str] = "geochem_test:GeochemDataset"
    class_name: ClassVar[str] = "GeochemDataset"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_TEST.GeochemDataset

    id: Union[str, GeochemDatasetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    ber_data_source: Optional[str] = None
    uri: Optional[Union[str, URI]] = None
    entity_type: Optional[Union[Union[str, "EntityType"], list[Union[str, "EntityType"]]]] = empty_list()
    experiment_type: Optional[Union[str, "ExperimentTypeEnum"]] = None
    coordinates: Optional[str] = None
    observations: Optional[Union[Union[dict, GeochemObservation], list[Union[dict, GeochemObservation]]]] = empty_list()
    experiment_metadata: Optional[Union[dict, TracerExperimentMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeochemDatasetId):
            self.id = GeochemDatasetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ber_data_source is not None and not isinstance(self.ber_data_source, str):
            self.ber_data_source = str(self.ber_data_source)

        if self.uri is not None and not isinstance(self.uri, URI):
            self.uri = URI(self.uri)

        if not isinstance(self.entity_type, list):
            self.entity_type = [self.entity_type] if self.entity_type is not None else []
        self.entity_type = [v if isinstance(v, EntityType) else EntityType(v) for v in self.entity_type]

        if self.experiment_type is not None and not isinstance(self.experiment_type, ExperimentTypeEnum):
            self.experiment_type = ExperimentTypeEnum(self.experiment_type)

        if self.coordinates is not None and not isinstance(self.coordinates, str):
            self.coordinates = str(self.coordinates)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=GeochemObservation, key_name="measurement_type", keyed=False)

        if self.experiment_metadata is not None and not isinstance(self.experiment_metadata, TracerExperimentMetadata):
            self.experiment_metadata = TracerExperimentMetadata(**as_dict(self.experiment_metadata))

        super().__post_init__(**kwargs)


# Enumerations
class GeochemMeasurementTypeEnum(EnumDefinitionImpl):
    """
    Types of geochemical measurements
    """
    radon_222 = PermissibleValue(
        text="radon_222",
        description="Radon-222 activity concentration",
        meaning=CHEBI["33323"])
    iodine = PermissibleValue(
        text="iodine",
        description="Iodine tracer concentration",
        meaning=CHEBI["24859"])
    cesium = PermissibleValue(
        text="cesium",
        description="Cesium tracer concentration",
        meaning=CHEBI["30514"])
    temperature = PermissibleValue(
        text="temperature",
        description="Water temperature",
        meaning=ENVO["09200014"])
    dissolved_oxygen = PermissibleValue(
        text="dissolved_oxygen",
        description="Dissolved oxygen concentration",
        meaning=ENVO["3100011"])
    specific_conductance = PermissibleValue(
        text="specific_conductance",
        description="Specific conductance of water",
        meaning=ENVO["09200013"])
    ph = PermissibleValue(
        text="ph",
        description="pH of water",
        meaning=ENVO["3100026"])
    orp = PermissibleValue(
        text="orp",
        description="Oxidation-reduction potential",
        meaning=ENVO["09200018"])

    _defn = EnumDefinition(
        name="GeochemMeasurementTypeEnum",
        description="Types of geochemical measurements",
    )

class ExperimentTypeEnum(EnumDefinitionImpl):
    """
    Types of well-field experiments
    """
    extraction = PermissibleValue(
        text="extraction",
        description="Groundwater extraction experiment")
    tracer = PermissibleValue(
        text="tracer",
        description="Tracer injection experiment")

    _defn = EnumDefinition(
        name="ExperimentTypeEnum",
        description="Types of well-field experiments",
    )

class EntityType(EnumDefinitionImpl):
    """
    Entity types from bertron-schema, representing categories of scientific data entities.
    """
    biodata = PermissibleValue(
        text="biodata",
        description="Biological data")
    sample = PermissibleValue(
        text="sample",
        description="Physical sample")
    sequence = PermissibleValue(
        text="sequence",
        description="Nucleotide or protein sequence")
    dataset = PermissibleValue(
        text="dataset",
        description="A collection of data")
    site = PermissibleValue(
        text="site",
        description="A geographic or experimental site")
    project = PermissibleValue(
        text="project",
        description="A research project")
    publication = PermissibleValue(
        text="publication",
        description="A published work")

    _defn = EnumDefinition(
        name="EntityType",
        description="Entity types from bertron-schema, representing categories of scientific data entities.",
    )

class BERSourceType(EnumDefinitionImpl):
    """
    Data source types from bertron-schema.
    """
    EMSL = PermissibleValue(
        text="EMSL",
        description="Environmental Molecular Sciences Laboratory")
    ESS_DIVE = PermissibleValue(
        text="ESS_DIVE",
        description="ESS-DIVE data repository")
    JGI = PermissibleValue(
        text="JGI",
        description="Joint Genome Institute")
    MONET = PermissibleValue(
        text="MONET",
        description="MONET consortium")
    NMDC = PermissibleValue(
        text="NMDC",
        description="National Microbiome Data Collaborative")

    _defn = EnumDefinition(
        name="BERSourceType",
        description="Data source types from bertron-schema.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=GEOCHEM_TEST.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=GEOCHEM_TEST.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=GEOCHEM_TEST.description, domain=None, range=Optional[str])

slots.ber_data_source = Slot(uri=GEOCHEM_TEST.ber_data_source, name="ber_data_source", curie=GEOCHEM_TEST.curie('ber_data_source'),
                   model_uri=GEOCHEM_TEST.ber_data_source, domain=None, range=Optional[str])

slots.uri = Slot(uri=GEOCHEM_TEST.uri, name="uri", curie=GEOCHEM_TEST.curie('uri'),
                   model_uri=GEOCHEM_TEST.uri, domain=None, range=Optional[Union[str, URI]])

slots.entity_type = Slot(uri=GEOCHEM_TEST.entity_type, name="entity_type", curie=GEOCHEM_TEST.curie('entity_type'),
                   model_uri=GEOCHEM_TEST.entity_type, domain=None, range=Optional[Union[Union[str, "EntityType"], list[Union[str, "EntityType"]]]])

slots.coordinates = Slot(uri=GEOCHEM_TEST.coordinates, name="coordinates", curie=GEOCHEM_TEST.curie('coordinates'),
                   model_uri=GEOCHEM_TEST.coordinates, domain=None, range=Optional[str])

slots.experiment_type = Slot(uri=GEOCHEM_TEST.experiment_type, name="experiment_type", curie=GEOCHEM_TEST.curie('experiment_type'),
                   model_uri=GEOCHEM_TEST.experiment_type, domain=None, range=Optional[Union[str, "ExperimentTypeEnum"]])

slots.sample_name = Slot(uri=GEOCHEM_TEST.sample_name, name="sample_name", curie=GEOCHEM_TEST.curie('sample_name'),
                   model_uri=GEOCHEM_TEST.sample_name, domain=None, range=Optional[str])

slots.measurement_type = Slot(uri=GEOCHEM_TEST.measurement_type, name="measurement_type", curie=GEOCHEM_TEST.curie('measurement_type'),
                   model_uri=GEOCHEM_TEST.measurement_type, domain=None, range=Union[str, "GeochemMeasurementTypeEnum"])

slots.measurement_value = Slot(uri=GEOCHEM_TEST.measurement_value, name="measurement_value", curie=GEOCHEM_TEST.curie('measurement_value'),
                   model_uri=GEOCHEM_TEST.measurement_value, domain=None, range=Union[dict, Quantity])

slots.uncertainty = Slot(uri=GEOCHEM_TEST.uncertainty, name="uncertainty", curie=GEOCHEM_TEST.curie('uncertainty'),
                   model_uri=GEOCHEM_TEST.uncertainty, domain=None, range=Optional[Union[dict, Quantity]])

slots.time_since_start = Slot(uri=GEOCHEM_TEST.time_since_start, name="time_since_start", curie=GEOCHEM_TEST.curie('time_since_start'),
                   model_uri=GEOCHEM_TEST.time_since_start, domain=None, range=Optional[Union[dict, Quantity]])

slots.quantity_value = Slot(uri=GEOCHEM_TEST.quantity_value, name="quantity_value", curie=GEOCHEM_TEST.curie('quantity_value'),
                   model_uri=GEOCHEM_TEST.quantity_value, domain=None, range=Decimal)

slots.quantity_unit = Slot(uri=SCHEMA.unitCode, name="quantity_unit", curie=SCHEMA.curie('unitCode'),
                   model_uri=GEOCHEM_TEST.quantity_unit, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.tracerExperimentMetadata__initial_iodine_concentration = Slot(uri=GEOCHEM_TEST.initial_iodine_concentration, name="tracerExperimentMetadata__initial_iodine_concentration", curie=GEOCHEM_TEST.curie('initial_iodine_concentration'),
                   model_uri=GEOCHEM_TEST.tracerExperimentMetadata__initial_iodine_concentration, domain=None, range=Optional[Union[dict, Quantity]])

slots.tracerExperimentMetadata__initial_cesium_concentration = Slot(uri=GEOCHEM_TEST.initial_cesium_concentration, name="tracerExperimentMetadata__initial_cesium_concentration", curie=GEOCHEM_TEST.curie('initial_cesium_concentration'),
                   model_uri=GEOCHEM_TEST.tracerExperimentMetadata__initial_cesium_concentration, domain=None, range=Optional[Union[dict, Quantity]])

slots.tracerExperimentMetadata__flow_rate = Slot(uri=GEOCHEM_TEST.flow_rate, name="tracerExperimentMetadata__flow_rate", curie=GEOCHEM_TEST.curie('flow_rate'),
                   model_uri=GEOCHEM_TEST.tracerExperimentMetadata__flow_rate, domain=None, range=Optional[Union[dict, Quantity]])

slots.geochemDataset__observations = Slot(uri=GEOCHEM_TEST.observations, name="geochemDataset__observations", curie=GEOCHEM_TEST.curie('observations'),
                   model_uri=GEOCHEM_TEST.geochemDataset__observations, domain=None, range=Optional[Union[Union[dict, GeochemObservation], list[Union[dict, GeochemObservation]]]])

slots.geochemDataset__experiment_metadata = Slot(uri=GEOCHEM_TEST.experiment_metadata, name="geochemDataset__experiment_metadata", curie=GEOCHEM_TEST.curie('experiment_metadata'),
                   model_uri=GEOCHEM_TEST.geochemDataset__experiment_metadata, domain=None, range=Optional[Union[dict, TracerExperimentMetadata]])

