from .base import TIOEndpoint

class AuditLogAPI(TIOEndpoint):
    def events(self, *filters, **kw):
        '''
        `audit-log: events <https://cloud.tenable.com/api#/resources/audit-log/events>`_

        Args:
            *filters (tuple, optional):
                Filters to allow the user to get to a specific subset of data
                within the audit log.  For a more detailed listing of what
                filters are available, please refer to the API documentation
                linked above, however some examples are as such:

                - ``('date', 'gt', '2017-07-05')``
                - ``('date', 'lt', '2017-07-07')``
                - ``('actor_id', 'match', '6000a811-8422-4096-83d3-e4d44f44b97d')``
                - ``('target_id', 'match', '6000a811-8422-4096-83d3-e4d44f44b97d')``

            limit (int, optional):
                The limit of how many events to return.  The API will default to
                50 unless otherwise specifified.

        Returns:
            list: List of event records
        '''
        return self._api.get('audit-log/v1/events', params={
            'f': ['{}:{}:{}'.format(
                self._check('filter_field_name', f[0], str),
                self._check('filter_operator', f[1], str),
                self._check('filter_value', f[2], str)) for f in filters],
            'limit': self._check('limit', kw['limit'], int) if 'limit' in kw else 50
        }).json()['events']
