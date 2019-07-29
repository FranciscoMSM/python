# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CustomResourceDefinitionStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accepted_names': 'V1beta1CustomResourceDefinitionNames',
        'conditions': 'list[V1beta1CustomResourceDefinitionCondition]',
        'stored_versions': 'list[str]'
    }

    attribute_map = {
        'accepted_names': 'acceptedNames',
        'conditions': 'conditions',
        'stored_versions': 'storedVersions'
    }

    def __init__(self, accepted_names=None, conditions=None, stored_versions=None):
        """
        V1beta1CustomResourceDefinitionStatus - a model defined in Swagger
        """

        self._accepted_names = None
        self._conditions = None
        self._stored_versions = None
        self.discriminator = None

        self.accepted_names = accepted_names
        self.conditions = conditions
        self.stored_versions = stored_versions

    @property
    def accepted_names(self):
        """
        Gets the accepted_names of this V1beta1CustomResourceDefinitionStatus.
        AcceptedNames are the names that are actually being used to serve discovery They may be different than the names in spec.

        :return: The accepted_names of this V1beta1CustomResourceDefinitionStatus.
        :rtype: V1beta1CustomResourceDefinitionNames
        """
        return self._accepted_names

    @accepted_names.setter
    def accepted_names(self, accepted_names):
        """
        Sets the accepted_names of this V1beta1CustomResourceDefinitionStatus.
        AcceptedNames are the names that are actually being used to serve discovery They may be different than the names in spec.

        :param accepted_names: The accepted_names of this V1beta1CustomResourceDefinitionStatus.
        :type: V1beta1CustomResourceDefinitionNames
        """
        if accepted_names is None:
            raise ValueError("Invalid value for `accepted_names`, must not be `None`")

        self._accepted_names = accepted_names

    @property
    def conditions(self):
        """
        Gets the conditions of this V1beta1CustomResourceDefinitionStatus.
        Conditions indicate state for particular aspects of a CustomResourceDefinition

        :return: The conditions of this V1beta1CustomResourceDefinitionStatus.
        :rtype: list[V1beta1CustomResourceDefinitionCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1beta1CustomResourceDefinitionStatus.
        Conditions indicate state for particular aspects of a CustomResourceDefinition

        :param conditions: The conditions of this V1beta1CustomResourceDefinitionStatus.
        :type: list[V1beta1CustomResourceDefinitionCondition]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")

        self._conditions = conditions

    @property
    def stored_versions(self):
        """
        Gets the stored_versions of this V1beta1CustomResourceDefinitionStatus.
        StoredVersions are all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so the migration controller can first finish a migration to another version (i.e. that no old objects are left in the storage), and then remove the rest of the versions from this list. None of the versions in this list can be removed from the spec.Versions field.

        :return: The stored_versions of this V1beta1CustomResourceDefinitionStatus.
        :rtype: list[str]
        """
        return self._stored_versions

    @stored_versions.setter
    def stored_versions(self, stored_versions):
        """
        Sets the stored_versions of this V1beta1CustomResourceDefinitionStatus.
        StoredVersions are all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so the migration controller can first finish a migration to another version (i.e. that no old objects are left in the storage), and then remove the rest of the versions from this list. None of the versions in this list can be removed from the spec.Versions field.

        :param stored_versions: The stored_versions of this V1beta1CustomResourceDefinitionStatus.
        :type: list[str]
        """
        if stored_versions is None:
            raise ValueError("Invalid value for `stored_versions`, must not be `None`")

        self._stored_versions = stored_versions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CustomResourceDefinitionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
