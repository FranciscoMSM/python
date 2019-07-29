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


class V1beta1WebhookClientConfig(object):
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
        'ca_bundle': 'str',
        'service': 'AdmissionregistrationV1beta1ServiceReference',
        'url': 'str'
    }

    attribute_map = {
        'ca_bundle': 'caBundle',
        'service': 'service',
        'url': 'url'
    }

    def __init__(self, ca_bundle=None, service=None, url=None):
        """
        V1beta1WebhookClientConfig - a model defined in Swagger
        """

        self._ca_bundle = None
        self._service = None
        self._url = None
        self.discriminator = None

        self.ca_bundle = ca_bundle
        if service is not None:
          self.service = service
        if url is not None:
          self.url = url

    @property
    def ca_bundle(self):
        """
        Gets the ca_bundle of this V1beta1WebhookClientConfig.
        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. Required.

        :return: The ca_bundle of this V1beta1WebhookClientConfig.
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """
        Sets the ca_bundle of this V1beta1WebhookClientConfig.
        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. Required.

        :param ca_bundle: The ca_bundle of this V1beta1WebhookClientConfig.
        :type: str
        """
        if ca_bundle is None:
            raise ValueError("Invalid value for `ca_bundle`, must not be `None`")
        if ca_bundle is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', ca_bundle):
            raise ValueError("Invalid value for `ca_bundle`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._ca_bundle = ca_bundle

    @property
    def service(self):
        """
        Gets the service of this V1beta1WebhookClientConfig.
        `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.  If the webhook is running within the cluster, then you should use `service`.  Port 443 will be used if it is open, otherwise it is an error.

        :return: The service of this V1beta1WebhookClientConfig.
        :rtype: AdmissionregistrationV1beta1ServiceReference
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this V1beta1WebhookClientConfig.
        `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.  If the webhook is running within the cluster, then you should use `service`.  Port 443 will be used if it is open, otherwise it is an error.

        :param service: The service of this V1beta1WebhookClientConfig.
        :type: AdmissionregistrationV1beta1ServiceReference
        """

        self._service = service

    @property
    def url(self):
        """
        Gets the url of this V1beta1WebhookClientConfig.
        `url` gives the location of the webhook, in standard URL form (`[scheme://]host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.

        :return: The url of this V1beta1WebhookClientConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this V1beta1WebhookClientConfig.
        `url` gives the location of the webhook, in standard URL form (`[scheme://]host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.

        :param url: The url of this V1beta1WebhookClientConfig.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, V1beta1WebhookClientConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
