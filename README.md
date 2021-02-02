# DEPRECATED

**This module is deprecated.** As of Feb. 2021, RNK website does not provide PDF summary of the stats anymore, but via an Arcgis-based interactive map `Corona Dashboard`.
Although it is very nice that they now provide interactive plots, but it is a pity that they chose Arcgis, it is super slow and not mobile-ready.

However, one good thing is that it provides a JSON api, you can use the form below to query data from the database:

https://services7.arcgis.com/0Uc5jDlEgdLosloE/arcgis/rest/services/dbdata_hd_rnk03/FeatureServer/0

Since it is possible to obtain data from the official database, it seems that this module is no longer useful - therefore it is deprecated.

# COVID-19 statistics of Heidelberg and Rhein-Neckar-Kreis

Data source: https://www.rhein-neckar-kreis.de/start/landratsamt/coronavirus+fallzahlen.html

A python module to automatically download/parse PDF summaries provided by Landratsamt RNK.
This module is used to plot data at https://pjb7687.github.io/covid19hd.html.

For details please refer to the `CoronaStats.ipynb`.

# License

BSD 2-Clause License

Copyright (c) 2021, Jeongbin Park
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
