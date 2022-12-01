# -*- coding: utf-8 -*-
"""
ElementsWorker methods for classifications and ML classes.
"""

from typing import Dict, List, Optional, Union

from apistar.exceptions import ErrorResponse
from peewee import IntegrityError

from arkindex_worker import logger
from arkindex_worker.cache import CachedClassification, CachedElement
from arkindex_worker.models import Element


class ClassificationMixin(object):
    def load_corpus_classes(self):
        """
        Load all ML classes available in the worker's corpus and store them in the ``self.classes`` cache.
        """
        corpus_classes = self.api_client.paginate(
            "ListCorpusMLClasses",
            id=self.corpus_id,
        )
        self.classes[self.corpus_id] = {
            ml_class["name"]: ml_class["id"] for ml_class in corpus_classes
        }
        logger.info(f"Loaded {len(self.classes[self.corpus_id])} ML classes")

    def get_ml_class_id(self, ml_class: str) -> str:
        """
        Return the MLClass ID corresponding to the given class name on a specific corpus.

        If no MLClass exists for this class name, a new one is created.
        :param ml_class: Name of the MLClass.
        :returns: ID of the retrieved or created MLClass.
        """
        if not self.classes.get(self.corpus_id):
            self.load_corpus_classes()

        ml_class_id = self.classes[self.corpus_id].get(ml_class)
        if ml_class_id is None:
            logger.info(f"Creating ML class {ml_class} on corpus {self.corpus_id}")
            try:
                response = self.request(
                    "CreateMLClass", id=self.corpus_id, body={"name": ml_class}
                )
                ml_class_id = self.classes[self.corpus_id][ml_class] = response["id"]
                logger.debug(f"Created ML class {response['id']}")
            except ErrorResponse as e:
                # Only reload for 400 errors
                if e.status_code != 400:
                    raise

                # Reload and make sure we have the class
                logger.info(
                    f"Reloading corpus classes to see if {ml_class} already exists"
                )
                self.load_corpus_classes()
                assert (
                    ml_class in self.classes[self.corpus_id]
                ), "Missing class {ml_class} even after reloading"
                ml_class_id = self.classes[self.corpus_id][ml_class]

        return ml_class_id

    def create_classification(
        self,
        element: Union[Element, CachedElement],
        ml_class: str,
        confidence: float,
        high_confidence: Optional[bool] = False,
    ) -> Dict[str, str]:
        """
        Create a classification on the given element through the API.

        :param element: The element to create a classification on.
        :param ml_class: Name of the MLClass to use.
        :param confidence: Confidence score for the classification. Must be between 0 and 1.
        :param high_confidence: Whether or not the classification is of high confidence.
        :returns: The created classification, as returned by the ``CreateClassification`` API endpoint.
        """
        assert element and isinstance(
            element, (Element, CachedElement)
        ), "element shouldn't be null and should be an Element or CachedElement"
        assert ml_class and isinstance(
            ml_class, str
        ), "ml_class shouldn't be null and should be of type str"
        assert (
            isinstance(confidence, float) and 0 <= confidence <= 1
        ), "confidence shouldn't be null and should be a float in [0..1] range"
        assert isinstance(
            high_confidence, bool
        ), "high_confidence shouldn't be null and should be of type bool"
        if self.is_read_only:
            logger.warning(
                "Cannot create classification as this worker is in read-only mode"
            )
            return

        try:
            created = self.request(
                "CreateClassification",
                body={
                    "element": str(element.id),
                    "ml_class": self.get_ml_class_id(ml_class),
                    "worker_run_id": self.worker_run_id,
                    "confidence": confidence,
                    "high_confidence": high_confidence,
                },
            )

            if self.use_cache:
                # Store classification in local cache
                try:
                    to_insert = [
                        {
                            "id": created["id"],
                            "element_id": element.id,
                            "class_name": ml_class,
                            "confidence": created["confidence"],
                            "state": created["state"],
                            "worker_run_id": self.worker_run_id,
                        }
                    ]
                    CachedClassification.insert_many(to_insert).execute()
                except IntegrityError as e:
                    logger.warning(
                        f"Couldn't save created classification in local cache: {e}"
                    )
        except ErrorResponse as e:
            # Detect already existing classification
            if e.status_code == 400 and "non_field_errors" in e.content:
                if (
                    "The fields element, worker_version, ml_class must make a unique set."
                    in e.content["non_field_errors"]
                ):
                    logger.warning(
                        f"This worker version has already set {ml_class} on element {element.id}"
                    )
                elif (
                    "The fields element, worker_run, ml_class must make a unique set."
                    in e.content["non_field_errors"]
                ):
                    logger.warning(
                        f"This worker run has already set {ml_class} on element {element.id}"
                    )
                else:
                    raise
                return

            # Propagate any other API error
            raise

        self.report.add_classification(element.id, ml_class)

        return created

    def create_classifications(
        self,
        element: Union[Element, CachedElement],
        classifications: List[Dict[str, Union[str, float, bool]]],
    ) -> List[Dict[str, Union[str, float, bool]]]:
        """
        Create multiple classifications at once on the given element through the API.

        :param element: The element to create classifications on.
        :param classifications: The classifications to create, a list of dicts. Each of them contains
            a **class_name** (str), the name of the MLClass for this classification;
            a **confidence** (float), the confidence score, between 0 and 1;
            a **high_confidence** (bool), the high confidence state of the classification.

        :returns: List of created classifications, as returned in the ``classifications`` field by
           the ``CreateClassifications`` API endpoint.
        """
        assert element and isinstance(
            element, (Element, CachedElement)
        ), "element shouldn't be null and should be an Element or CachedElement"
        assert classifications and isinstance(
            classifications, list
        ), "classifications shouldn't be null and should be of type list"

        for index, classification in enumerate(classifications):
            class_name = classification.get("class_name")
            assert class_name and isinstance(
                class_name, str
            ), f"Classification at index {index} in classifications: class_name shouldn't be null and should be of type str"

            confidence = classification.get("confidence")
            assert (
                confidence is not None
                and isinstance(confidence, float)
                and 0 <= confidence <= 1
            ), f"Classification at index {index} in classifications: confidence shouldn't be null and should be a float in [0..1] range"

            high_confidence = classification.get("high_confidence")
            if high_confidence is not None:
                assert isinstance(
                    high_confidence, bool
                ), f"Classification at index {index} in classifications: high_confidence should be of type bool"

        if self.is_read_only:
            logger.warning(
                "Cannot create classifications as this worker is in read-only mode"
            )
            return

        created_cls = self.request(
            "CreateClassifications",
            body={
                "parent": str(element.id),
                "worker_run_id": self.worker_run_id,
                "classifications": classifications,
            },
        )["classifications"]

        for created_cl in created_cls:
            self.report.add_classification(element.id, created_cl["class_name"])

        if self.use_cache:
            # Store classifications in local cache
            try:
                to_insert = [
                    {
                        "id": created_cl["id"],
                        "element_id": element.id,
                        "class_name": created_cl["class_name"],
                        "confidence": created_cl["confidence"],
                        "state": created_cl["state"],
                        "worker_run_id": self.worker_run_id,
                    }
                    for created_cl in created_cls
                ]
                CachedClassification.insert_many(to_insert).execute()
            except IntegrityError as e:
                logger.warning(
                    f"Couldn't save created classifications in local cache: {e}"
                )

        return created_cls
