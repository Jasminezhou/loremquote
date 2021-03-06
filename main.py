#!/usr/bin/env python
#
# Copyright 2015 Jing Studio.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random


CATEGORIES = {
    'confucious': 'quotes/confucious.txt',
    'wise': 'quotes/wise_quotes.txt'}


def random_line(afile):
    return random.choice(open(afile).readlines())


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class APIHandler(webapp2.RequestHandler):
    def get(self, category):
        if category in CATEGORIES:
            self.response.write(random_line(CATEGORIES[category]))
        else:
            self.response.write(random_line(CATEGORIES['confucious']))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api/([^/]+)', APIHandler),
], debug=True)
