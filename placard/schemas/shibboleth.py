# Copyright 2012 VPAC
#
# This file is part of django-tldap.
#
# django-tldap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-tldap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-tldap  If not, see <http://www.gnu.org/licenses/>.

class shibbolethMixin(object):
    def _generate_shared_token(self):
        try:
            from hashlib import sha
        except:
            from sha import sha
        import base64
        uid = self.uid
        mail = self.mail
        entityID = django.conf.settings.SHIBBOLETH_URL
        salt = django.conf.settings.SHIBBOLETH_SALT
        return base64.urlsafe_b64encode(sha(uid + mail + entityID + salt).digest())[:-1]

    def set_shibboleth_defaults(self):
        pass

    def save_shibboleth_defaults(self):
        if self.auEduPersonSharedToken is None:
            self.auEduPersonSharedToken = self._generate_shared_token()

    def shibboleth_lock(self):
        self.eduPersonAffiliation = 'affiliate'

    def shibboleth_unlock(self):
        self.edupersonaffiliation = 'staff'
