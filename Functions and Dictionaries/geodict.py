#dictionaries of geographies and formatting for GEO_IDs/FIPS etc.
#this dict has the Census Bureau default naming convention as the key, and the value we want to see in our docs as the value

namestocommon = {'Williamson County, TN': 'Williamson County',
                  'Wilson County, TN': 'Wilson County',
                  'Houston County, TN': 'Houston County',
                  'Humphreys County, TN': 'Humphreys County',
                  'Macon County, TN': 'Macon County',
                  'Maury County, TN': 'Maury County',
                  'Montgomery County, TN': 'Montgomery County',
                  'Rutherford County, TN': 'Rutherford County',
                  'Robertson County, TN': 'Robertson County',
                  'Stewart County, TN': 'Stewart County',
                  'Sumner County, TN': 'Sumner County',
                  'Trousdale County, TN': 'Trousdale County',
                  'Hartsville/Trousdale County, TN': 'Hartsville/Trousdale County',
                  'Cheatham County, TN': 'Cheatham County',
                  'Davidson County, TN': 'Davidson County',
                  'Dickson County, TN': 'Dickson County',
                  'Williamson County, Tennessee': 'Williamson County',
                  'Wilson County, Tennessee': 'Wilson County',
                  'Houston County, Tennessee': 'Houston County',
                  'Humphreys County, Tennessee': 'Humphreys County',
                  'Macon County, Tennessee': 'Macon County',
                  'Maury County, Tennessee': 'Maury County',
                  'Montgomery County, Tennessee': 'Montgomery County',
                  'Rutherford County, Tennessee': 'Rutherford County',
                  'Robertson County, Tennessee': 'Robertson County',
                  'Stewart County, Tennessee': 'Stewart County',
                  'Sumner County, Tennessee': 'Sumner County',
                  'Trousdale County, Tennessee': 'Trousdale County',
                  'Hartsville/Trousdale County, Tennessee': 'Hartsville/Trousdale County',
                  'Cheatham County, Tennessee': 'Cheatham County',
                  'Davidson County, Tennessee': 'Davidson County',
                  'Dickson County, Tennessee': 'Dickson County',
                  'Simpson County, KY': 'Simpson County, KY',
                  'Allen County, KY': 'Allen County, KY',
                  'Simpson County, Kentucky': 'Simpson County, KY',
                  'Allen County, Kentucky': 'Allen County, KY',
                  'Nolensville town, TN': 'Nolensville',
                  'Adams city, TN': 'Adams',
                  'Orlinda city, TN': 'Orlinda',
                  'Ashland City town, TN': 'Ashland City',
                  'Belle Meade city, TN': 'Belle Meade',
                  'Oak Hill city, TN': 'Oak Hill',
                  'Pegram town, TN': 'Pegram',
                  'Portland city, TN': 'Portland',
                  'Pleasant View city, TN': 'Pleasant View',
                  'Ridgetop city, TN': 'Ridgetop',
                  'Berry Hill city, TN': 'Berry Hill',
                  'Brentwood city, TN': 'Brentwood',
                  'Burns town, TN': 'Burns',
                  'Hendersonville city, TN': 'Hendersonville',
                  'Kingston Springs town, TN': 'Kingston Springs',
                  'Lafayette city, TN': 'Lafayette',
                  'La Vergne city, TN': 'La Vergne',
                  'Lebanon city, TN': 'Lebanon',
                  'McEwen city, TN': 'McEwen',
                  'Millersville city, TN': 'Millersville',
                  'Mitchellville city, TN': 'Mitchellville',
                  'Mount Juliet city, TN': 'Mount Juliet',
                  'Mount Pleasant city, TN': 'Mount Pleasant',
                  'Murfreesboro city, TN': 'Murfreesboro',
                  'Nashville-Davidson metropolitan government (balance), TN': 'Nashville',
                  'New Johnsonville city, TN': 'New Johnsonville',
                  'Vanleer town, TN': 'Vanleer',
                  'Watertown city, TN': 'Watertown',
                  'Waverly city, TN': 'Waverly',
                  'Westmoreland town, TN': 'Westmoreland',
                  'White Bluff town, TN': 'White Bluff',
                  'White House city, TN': 'White House',
                  'Eagleville city, TN': 'Eagleville',
                  'Erin city, TN': 'Erin',
                  'Fairview city, TN': 'Fairview',
                  'Forest Hills city, TN': 'Forest Hills',
                  'Franklin city, TN': 'Franklin',
                  'Gallatin city, TN': 'Gallatin',
                  'Goodlettsville city, TN': 'Goodlettsville',
                  'Greenbrier town, TN': 'Greenbrier',
                  'Cedar Hill city, TN': 'Cedar Hill',
                  'Charlotte town, TN': 'Charlotte',
                  'Clarksville city, TN': 'Clarksville',
                  'Coopertown town, TN': 'Coopertown',
                  'Columbia city, TN': 'Columbia',
                  'Cumberland City town, TN': 'Cumberland City',
                  'Cross Plains city, TN': 'Cross Plains',
                  'Dover city, TN': 'Dover',
                  'Smyrna town, TN': 'Smyrna',
                  'Slayden town, TN': 'Slayden',
                  'Springfield city, TN': 'Springfield',
                  'Spring Hill city, TN': 'Spring Hill',
                  'Tennessee Ridge town, TN': 'Tennessee Ridge',
                  "Thompson's Station town, TN": "Thompson's Station",
                  'Dickson city, TN': 'Dickson',
                  'Franklin city, TN': 'Franklin',
                  'Scottsville city, KY': 'Scottsville',
                  'Nolensville town, Tennessee': 'Nolensville',
                  'Adams city, Tennessee': 'Adams',
                  'Ashland City town, Tennessee': 'Ashland City',
                  'Belle Meade city, Tennessee': 'Belle Meade',
                  'Oak Hill city, Tennessee': 'Oak Hill',
                  'Pegram town, Tennessee': 'Pegram',
                  'Portland city, Tennessee': 'Portland',
                  'Pleasant View city, Tennessee': 'Pleasant View',
                  'Ridgetop city, Tennessee': 'Ridgetop',
                  'Berry Hill city, Tennessee': 'Berry Hill',
                  'Brentwood city, Tennessee': 'Brentwood',
                  'Burns town, Tennessee': 'Burns',
                  'Hendersonville city, Tennessee': 'Hendersonville',
                  'Kingston Springs town, Tennessee': 'Kingston Springs',
                  'Lafayette city, Tennessee': 'Lafayette',
                  'La Vergne city, Tennessee': 'La Vergne',
                  'Lebanon city, Tennessee': 'Lebanon',
                  'McEwen city, Tennessee': 'McEwen',
                  'Millersville city, Tennessee': 'Millersville',
                  'Mitchellville city, Tennessee': 'Mitchellville',
                  'Mount Juliet city, Tennessee': 'Mount Juliet',
                  'Mount Pleasant city, Tennessee': 'Mount Pleasant',
                  'Murfreesboro city, Tennessee': 'Murfreesboro',
                  'Nashville-Davidson metropolitan government (balance), Tennessee': 'Nashville',
                  'New Johnsonville city, Tennessee': 'New Johnsonville',
                  'Vanleer town, Tennessee': 'Vanleer',
                  'Watertown city, Tennessee': 'Watertown',
                  'Waverly city, Tennessee': 'Waverly',
                  'Westmoreland town, Tennessee': 'Westmoreland',
                  'White Bluff town, Tennessee': 'White Bluff',
                  'White House city, Tennessee': 'White House',
                  'Eagleville city, Tennessee': 'Eagleville',
                  'Erin city, Tennessee': 'Erin',
                  'Fairview city, Tennessee': 'Fairview',
                  'Forest Hills city, Tennessee': 'Forest Hills',
                  'Franklin city, Tennessee': 'Franklin',
                  'Gallatin city, Tennessee': 'Gallatin',
                  'Goodlettsville city, Tennessee': 'Goodlettsville',
                  'Greenbrier town, Tennessee': 'Greenbrier',
                  'Cedar Hill city, Tennessee': 'Cedar Hill',
                  'Charlotte town, Tennessee': 'Charlotte',
                  'Clarksville city, Tennessee': 'Clarksville',
                  'Coopertown town, Tennessee': 'Coopertown',
                  'Columbia city, Tennessee': 'Columbia',
                  'Cumberland City town, Tennessee': 'Cumberland City',
                  'Cross Plains city, Tennessee': 'Cross Plains',
                  'Dover city, Tennessee': 'Dover',
                  'Smyrna town, Tennessee': 'Smyrna',
                  'Slayden town, Tennessee': 'Slayden',
                  'Springfield city, Tennessee': 'Springfield',
                  'Spring Hill city, Tennessee': 'Spring Hill',
                  'Tennessee Ridge town, Tennessee': 'Tennessee Ridge',
                  "Thompson's Station town, Tennessee": "Thompson's Station",
                  'Dickson city, Tennessee': 'Dickson',
                  'Franklin city, Kentucky': 'Franklin',
                  'Scottsville city, Kentucky': 'Scottsville',
                  'Tennessee': 'Tennessee',
                  'United States': 'US',
                  'Tennessee (47)': 'Tennessee',
                  'Cheatham County, Tennessee (47021)': 'Cheatham County',
                  'Davidson County, Tennessee (47037)': 'Davidson County',
                  'Dickson County, Tennessee (47043)': 'Dickson County',
                  'Houston County, Tennessee (47083)': 'Houston County',
                  'Humphreys County, Tennessee (47085)': 'Humphreys County',
                  'Maury County, Tennessee (47119)': 'Maury County',
                  'Montgomery County, Tennessee (47125)': 'Montgomery County',
                  'Robertson County, Tennessee (47147)': 'Robertson County',
                  'Rutherford County, Tennessee (47149)': 'Rutherford County',
                  'Stewart County, Tennessee (47161)': 'Stewart County',
                  'Sumner County, Tennessee (47165)': 'Sumner County',
                  'Trousdale County, Tennessee (47169)': 'Trousdale County',
                  'Williamson County, Tennessee (47187)': 'Williamson County',
                  'Wilson County, Tennessee (47189)': 'Wilson County'
}

#to full census geo name
tofullcensus = {'Williamson County, TN': 'Williamson County, Tennessee',
                  'Wilson County, TN': 'Wilson County, Tennessee',
                  'Houston County, TN': 'Houston County, Tennessee',
                  'Humphreys County, TN': 'Humphreys County, Tennessee',
                  'Macon County, TN': 'Macon County, Tennessee',
                  'Maury County, TN': 'Maury County, Tennessee',
                  'Montgomery County, TN': 'Montgomery County, Tennessee',
                  'Rutherford County, TN': 'Rutherford County, Tennessee',
                  'Robertson County, TN': 'Robertson County, Tennessee',
                  'Stewart County, TN': 'Stewart County, Tennessee',
                  'Sumner County, TN': 'Sumner County, Tennessee',
                  'Trousdale County, TN': 'Trousdale County, Tennessee',
                  'Hartsville/Trousdale County, TN': 'Hartsville/Trousdale County, Tennessee',
                  'Cheatham County, TN': 'Cheatham County, Tennessee',
                  'Davidson County, TN': 'Davidson County, Tennessee',
                  'Dickson County, TN': 'Dickson County, Tennessee',
                  'Simpson County, KY': 'Simpson County, Kentucky',
                  'Allen County, KY': 'Allen County, Kentucky',
                  'Williamson County': 'Williamson County, Tennessee',
                  'Wilson County': 'Wilson County, Tennessee',
                  'Houston County': 'Houston County, Tennessee',
                  'Humphreys County': 'Humphreys County, Tennessee',
                  'Macon County': 'Macon County, Tennessee',
                  'Maury County': 'Maury County, Tennessee',
                  'Montgomery County': 'Montgomery County, Tennessee',
                  'Rutherford County': 'Rutherford County, Tennessee',
                  'Robertson County': 'Robertson County, Tennessee',
                  'Stewart County': 'Stewart County, Tennessee',
                  'Sumner County': 'Sumner County, Tennessee',
                  'Trousdale County': 'Trousdale County, Tennessee',
                  'Hartsville/Trousdale County': 'Hartsville/Trousdale County, Tennessee',
                  'Cheatham County': 'Cheatham County, Tennessee',
                  'Davidson County': 'Davidson County, Tennessee',
                  'Dickson County': 'Dickson County, Tennessee',
                  'Simpson County': 'Simpson County, Kentucky',
                  'Allen County': 'Allen County, Kentucky',
                  'Nolensville town, TN': 'Nolensville town, Tennessee',
                  'Adams city, TN': 'Adams city, Tennessee',
                  'Orlinda city, TN': 'Orlinda city, Tennessee',
                  'Orlinda': 'Orlinda city, Tennessee',
                  'Ashland City town, TN': 'Ashland City town, Tennessee',
                  'Belle Meade city, TN': 'Belle Meade city, Tennessee',
                  'Oak Hill city, TN': 'Oak Hill city, Tennessee',
                  'Pegram town, TN': 'Pegram town, Tennessee',
                  'Portland city, TN': 'Portland city, Tennessee',
                  'Pleasant View city, TN': 'Pleasant View city, Tennessee',
                  'Ridgetop city, TN': 'Ridgetop city, Tennessee',
                  'Berry Hill city, TN': 'Berry Hill city, Tennessee',
                  'Brentwood city, TN': 'Brentwood city, Tennessee',
                  'Burns town, TN': 'Burns town, Tennessee',
                  'Hendersonville city, TN': 'Hendersonville city, Tennessee',
                  'Kingston Springs town, TN': 'Kingston Springs town, Tennessee',
                  'Lafayette city, TN': 'Lafayette city, Tennessee',
                  'La Vergne city, TN': 'La Vergne city, Tennessee',
                  'Lebanon city, TN': 'Lebanon city, Tennessee',
                  'McEwen city, TN': 'McEwen city, Tennessee',
                  'Millersville city, TN': 'Millersville city, Tennessee',
                  'Mitchellville city, TN': 'Mitchellville city, Tennessee',
                  'Mount Juliet city, TN': 'Mount Juliet city, Tennessee',
                  'Mount Pleasant city, TN': 'Mount Pleasant city, Tennessee',
                  'Murfreesboro city, TN': 'Murfreesboro city, Tennessee',
                  'Nashville-Davidson metropolitan government (balance), TN': 'Nashville-Davidson metropolitan government (balance), Tennessee',
                  'New Johnsonville city, TN': 'New Johnsonville city, Tennessee',
                  'Vanleer town, TN': 'Vanleer town, Tennessee',
                  'Watertown city, TN': 'Watertown city, Tennessee',
                  'Waverly city, TN': 'Waverly city, Tennessee',
                  'Westmoreland town, TN': 'Westmoreland town, Tennessee',
                  'White Bluff town, TN': 'White Bluff town, Tennessee',
                  'White House city, TN': 'White House city, Tennessee',
                  'Eagleville city, TN': 'Eagleville city, Tennessee',
                  'Erin city, TN': 'Erin city, Tennessee',
                  'Fairview city, TN': 'Fairview city, Tennessee',
                  'Forest Hills city, TN': 'Forest Hills city, Tennessee',
                  'Franklin city, TN': 'Franklin city, Tennessee',
                  'Gallatin city, TN': 'Gallatin city, Tennessee',
                  'Goodlettsville city, TN': 'Goodlettsville city, Tennessee',
                  'Greenbrier town, TN': 'Greenbrier town, Tennessee',
                  'Cedar Hill city, TN': 'Cedar Hill city, Tennessee',
                  'Charlotte town, TN': 'Charlotte town, Tennessee',
                  'Clarksville city, TN': 'Clarksville city, Tennessee',
                  'Coopertown town, TN': 'Coopertown town, Tennessee',
                  'Columbia city, TN': 'Columbia city, Tennessee',
                  'Cumberland City town, TN': 'Cumberland City town, Tennessee',
                  'Cross Plains city, TN': 'Cross Plains city, Tennessee',
                  'Dover city, TN': 'Dover city, Tennessee',
                  'Smyrna town, TN': 'Smyrna town, Tennessee',
                  'Slayden town, TN': 'Slayden town, Tennessee',
                  'Springfield city, TN': 'Springfield city, Tennessee',
                  'Spring Hill city, TN': 'Spring Hill city, Tennessee',
                  'Tennessee Ridge town, TN': 'Tennessee Ridge town, Tennessee',
                  "Thompson's Station town, TN": "Thompson's Station town, Tennessee",
                  'Dickson city, TN': 'Dickson city, Tennessee',
                  'Franklin city, TN': 'Franklin city, Tennessee',
                  'Scottsville city, KY': 'Scottsville city, Kentucky',
                  'Nolensville': 'Nolensville town, Tennessee',
                  'Adams': 'Adams city, Tennessee',
                  'Ashland City': 'Ashland City town, Tennessee',
                  'Belle Meade': 'Belle Meade city, Tennessee',
                  'Oak Hill': 'Oak Hill city, Tennessee',
                  'Pegram': 'Pegram town, Tennessee',
                  'Portland': 'Portland city, Tennessee',
                  'Pleasant View': 'Pleasant View city, Tennessee',
                  'Ridgetop': 'Ridgetop city, Tennessee',
                  'Berry Hill': 'Berry Hill city, Tennessee',
                  'Brentwood': 'Brentwood city, Tennessee',
                  'Burns': 'Burns town, Tennessee',
                  'Hendersonville': 'Hendersonville city, Tennessee',
                  'Kingston Springs': 'Kingston Springs town, Tennessee',
                  'Lafayette': 'Lafayette city, Tennessee',
                  'La Vergne': 'La Vergne city, Tennessee',
                  'Lebanon': 'Lebanon city, Tennessee',
                  'McEwen': 'McEwen city, Tennessee',
                  'Millersville': 'Millersville city, Tennessee',
                  'Mitchellville': 'Mitchellville city, Tennessee',
                  'Mount Juliet': 'Mount Juliet city, Tennessee',
                  'Mount Pleasant': 'Mount Pleasant city, Tennessee',
                  'Murfreesboro': 'Murfreesboro city, Tennessee',
                  'Nashville': 'Nashville-Davidson metropolitan government (balance), Tennessee',
                  'New Johnsonville': 'New Johnsonville city, Tennessee',
                  'Vanleer': 'Vanleer town, Tennessee',
                  'Watertown': 'Watertown city, Tennessee',
                  'Waverly': 'Waverly city, Tennessee',
                  'Westmoreland': 'Westmoreland town, Tennessee',
                  'White Bluff': 'White Bluff town, Tennessee',
                  'White House': 'White House city, Tennessee',
                  'Eagleville': 'Eagleville city, Tennessee',
                  'Erin': 'Erin city, Tennessee',
                  'Fairview': 'Fairview city, Tennessee',
                  'Forest Hills': 'Forest Hills city, Tennessee',
                  'Franklin': 'Franklin city, Kentucky',
                  'Gallatin': 'Gallatin city, Tennessee',
                  'Goodlettsville': 'Goodlettsville city, Tennessee',
                  'Greenbrier': 'Greenbrier town, Tennessee',
                  'Cedar Hill': 'Cedar Hill city, Tennessee',
                  'Charlotte': 'Charlotte town, Tennessee',
                  'Clarksville': 'Clarksville city, Tennessee',
                  'Coopertown': 'Coopertown town, Tennessee',
                  'Columbia': 'Columbia city, Tennessee',
                  'Cumberland City': 'Cumberland City town, Tennessee',
                  'Cross Plains': 'Cross Plains city, Tennessee',
                  'Dover': 'Dover city, Tennessee',
                  'Smyrna': 'Smyrna town, Tennessee',
                  'Slayden': 'Slayden town, Tennessee',
                  'Springfield': 'Springfield city, Tennessee',
                  'Spring Hill': 'Spring Hill city, Tennessee',
                  'Tennessee Ridge': 'Tennessee Ridge town, Tennessee',
                  "Thompson's Station": "Thompson's Station town, Tennessee",
                  'Dickson': 'Dickson city, Tennessee',
                  'Scottsville': 'Scottsville city, Kentucky',
                  'US': 'United States',
                  'USA': 'United States',
                  'Tennessee (47)': 'Tennessee',
                  'Cheatham County, Tennessee (47021)': 'Cheatham County, Tennessee',
                  'Davidson County, Tennessee (47037)': 'Davidson County, Tennessee',
                  'Dickson County, Tennessee (47043)': 'Dickson County, Tennessee',
                  'Houston County, Tennessee (47083)': 'Houston County, Tennessee',
                  'Humphreys County, Tennessee (47085)': 'Humphreys County, Tennessee',
                  'Maury County, Tennessee (47119)': 'Maury County, Tennessee',
                  'Montgomery County, Tennessee (47125)': 'Montgomery County, Tennessee',
                  'Robertson County, Tennessee (47147)': 'Robertson County, Tennessee',
                  'Rutherford County, Tennessee (47149)': 'Rutherford County, Tennessee',
                  'Stewart County, Tennessee (47161)': 'Stewart County, Tennessee',
                  'Sumner County, Tennessee (47165)': 'Sumner County, Tennessee',
                  'Trousdale County, Tennessee (47169)': 'Trousdale County, Tennessee',
                  'Williamson County, Tennessee (47187)': 'Williamson County, Tennessee',
                  'Wilson County, Tennessee (47189)': 'Wilson County, Tennessee'}
#this dict has the common use name to the full geoid
geotogeoid = {'Williamson County': '0500000US47187',
                 'Wilson County': '0500000US47189',
                 'Houston County': '0500000US47083',
                 'Humphreys County': '0500000US47085',
                 'Macon County': '0500000US47111',
                 'Maury County': '0500000US47119',
                 'Montgomery County': '0500000US47125',
                 'Rutherford County': '0500000US47149',
                 'Robertson County': '0500000US47147',
                 'Stewart County': '0500000US47161',
                 'Sumner County': '0500000US47165',
                 'Trousdale County': '0500000US47169',
                 'Cheatham County': '0500000US47021',
                 'Davidson County': '0500000US47037',
                 'Dickson County': '0500000US47043',
                 'Simpson County, KY': '0500000US21213',
                 'Allen County, KY': '0500000US21003',
                 'Nolensville': '1600000US4753460',
                 'Adams': '1600000US4700200',
                 'Ashland City': '1600000US4702180',
                 'Belle Meade': '1600000US4704620',
                 'Oak Hill': '1600000US4754780',
                 'Pegram': '1600000US4757480',
                 'Portland': '1600000US4760280',
                 'Pleasant View': '1600000US4759560',
                 'Ridgetop': '1600000US4763140',
                 'Berry Hill': '1600000US4705140',
                 'Brentwood': '1600000US4708280',
                 'Burns': '1600000US4709880',
                 'Hendersonville': '1600000US4733280',
                 'Kingston Springs': '1600000US4739660',
                 'Lafayette': '1600000US4740160',
                 'La Vergne': '1600000US4741200',
                 'Lebanon': '1600000US4741520',
                 'McEwen': '1600000US4744840',
                 'Millersville': '1600000US4748980',
                 'Mitchellville': '1600000US4749460',
                 'Mount Juliet': '1600000US4750780',
                 'Mount Pleasant': '1600000US4751080',
                 'Murfreesboro': '1600000US4751560',
                 'Nashville': '1600000US4752006',
                 'New Johnsonville': '1600000US4752820',
                 'Vanleer': '1600000US4776860',
                 'Watertown': '1600000US4778320',
                 'Waverly': '1600000US4778560',
                 'Westmoreland': '1600000US4779420',
                 'White Bluff': '1600000US4779980',
                 'White House': '1600000US4780200',
                 'Eagleville': '1600000US4722360',
                 'Erin': '1600000US4724320',
                 'Fairview': '1600000US4725440',
                 'Forest Hills': '1600000US4727020',
                 'Franklin': '1600000US4727740',
                 'Gallatin': '1600000US4728540',
                 'Goodlettsville': '1600000US4729920',
                 'Greenbrier': '1600000US4730960',
                 'Cedar Hill': '1600000US4711980',
                 'Charlotte': '1600000US4713080',
                 'Clarksville': '1600000US4715160',
                 'Coopertown': '1600000US4716980',
                 'Columbia': '1600000US4716540',
                 'Cumberland City': '1600000US4718820',
                 'Cross Plains': '1600000US4718420',
                 'Dover': '1600000US4721400',
                 'Smyrna': '1600000US4769420',
                 'Slayden': '1600000US4769080',
                 'Springfield': '1600000US4770500',
                 'Spring Hill': '1600000US4770580',
                 'Tennessee Ridge': '1600000US4773460',
                 "Thompson's Station": '1600000US4773900',
                 'Dickson': '1600000US4720620',
                 'Franklin': '1600000US2128918',
                 'Scottsville': '1600000US2169114',
                 'Tennessee': '0400000US47',
                 'US': '0100000US',
                 'Williamson County, Tennessee': '0500000US47187',
                 'Wilson County, Tennessee': '0500000US47189',
                 'Houston County, Tennessee': '0500000US47083',
                 'Humphreys County, Tennessee': '0500000US47085',
                 'Macon County, Tennessee': '0500000US47111',
                 'Maury County, Tennessee': '0500000US47119',
                 'Montgomery County, Tennessee': '0500000US47125',
                 'Rutherford County, Tennessee': '0500000US47149',
                 'Robertson County, Tennessee': '0500000US47147',
                 'Stewart County, Tennessee': '0500000US47161',
                 'Sumner County, Tennessee': '0500000US47165',
                 'Trousdale County, Tennessee': '0500000US47169',
                 'Cheatham County, Tennessee': '0500000US47021',
                 'Davidson County, Tennessee': '0500000US47037',
                 'Dickson County, Tennessee': '0500000US47043',
                 'Simpson County, Kentucky': '0500000US21213',
                 'Allen County, Kentucky': '0500000US21003',
                 'Nolensville town, Tennessee': '1600000US4753460',
                 'Adams city, Tennessee': '1600000US4700200',
                 'Ashland City town, Tennessee': '1600000US4702180',
                 'Belle Meade city, Tennessee': '1600000US4704620',
                 'Oak Hill city, Tennessee': '1600000US4754780',
                 'Pegram town, Tennessee': '1600000US4757480',
                 'Portland city, Tennessee': '1600000US4760280',
                 'Pleasant View city, Tennessee': '1600000US4759560',
                 'Ridgetop city, Tennessee': '1600000US4763140',
                 'Berry Hill city, Tennessee': '1600000US4705140',
                 'Brentwood city, Tennessee': '1600000US4708280',
                 'Burns town, Tennessee': '1600000US4709880',
                 'Hendersonville city, Tennessee': '1600000US4733280',
                 'Kingston Springs town, Tennessee': '1600000US4739660',
                 'Lafayette city, Tennessee': '1600000US4740160',
                 'La Vergne city, Tennessee': '1600000US4741200',
                 'Lebanon city, Tennessee': '1600000US4741520',
                 'McEwen city, Tennessee': '1600000US4744840',
                 'Millersville city, Tennessee': '1600000US4748980',
                 'Mitchellville city, Tennessee': '1600000US4749460',
                 'Mount Juliet city, Tennessee': '1600000US4750780',
                 'Mount Pleasant city, Tennessee': '1600000US4751080',
                 'Murfreesboro city, Tennessee': '1600000US4751560',
                 'Nashville-Davidson metropolitan government (balance), Tennessee': '1600000US4752006',
                 'New Johnsonville city, Tennessee': '1600000US4752820',
                 'Vanleer town, Tennessee': '1600000US4776860',
                 'Watertown city, Tennessee': '1600000US4778320',
                 'Waverly city, Tennessee': '1600000US4778560',
                 'Westmoreland town, Tennessee': '1600000US4779420',
                 'White Bluff town, Tennessee': '1600000US4779980',
                 'White House city, Tennessee': '1600000US4780200',
                 'Eagleville city, Tennessee': '1600000US4722360',
                 'Erin city, Tennessee': '1600000US4724320',
                 'Fairview city, Tennessee': '1600000US4725440',
                 'Forest Hills city, Tennessee': '1600000US4727020',
                 'Franklin city, Tennessee': '1600000US4727740',
                 'Gallatin city, Tennessee': '1600000US4728540',
                 'Goodlettsville city, Tennessee': '1600000US4729920',
                 'Greenbrier town, Tennessee': '1600000US4730960',
                 'Cedar Hill city, Tennessee': '1600000US4711980',
                 'Charlotte town, Tennessee': '1600000US4713080',
                 'Clarksville city, Tennessee': '1600000US4715160',
                 'Coopertown town, Tennessee': '1600000US4716980',
                 'Columbia city, Tennessee': '1600000US4716540',
                 'Cumberland City town, Tennessee': '1600000US4718820',
                 'Cross Plains city, Tennessee': '1600000US4718420',
                 'Dover city, Tennessee': '1600000US4721400',
                 'Smyrna town, Tennessee': '1600000US4769420',
                 'Slayden town, Tennessee': '1600000US4769080',
                 'Springfield city, Tennessee': '1600000US4770500',
                 'Spring Hill city, Tennessee': '1600000US4770580',
                 'Tennessee Ridge town, Tennessee': '1600000US4773460',
                 "Thompson's Station town, Tennessee": '1600000US4773900',
                 'Dickson city, Tennessee': '1600000US4720620',
                 'Franklin city, Kentucky': '1600000US2128918',
                 'Scottsville city, Kentucky': '1600000US2169114',
                 'Williamson County, TN': '0500000US47187',
                 'Wilson County, TN': '0500000US47189',
                 'Houston County, TN': '0500000US47083',
                 'Humphreys County, TN': '0500000US47085',
                 'Macon County, TN': '0500000US47111',
                 'Maury County, TN': '0500000US47119',
                 'Montgomery County, TN': '0500000US47125',
                 'Rutherford County, TN': '0500000US47149',
                 'Robertson County, TN': '0500000US47147',
                 'Stewart County, TN': '0500000US47161',
                 'Sumner County, TN': '0500000US47165',
                 'Trousdale County, TN': '0500000US47169',
                 'Cheatham County, TN': '0500000US47021',
                 'Davidson County, TN': '0500000US47037',
                 'Dickson County, TN': '0500000US47043',
                 'Simpson County, KY': '0500000US21213',
                 'Allen County, KY': '0500000US21003',
                 'Nolensville town, TN': '1600000US4753460',
                 'Adams city, TN': '1600000US4700200',
                 'Ashland City town, TN': '1600000US4702180',
                 'Belle Meade city, TN': '1600000US4704620',
                 'Oak Hill city, TN': '1600000US4754780',
                 'Pegram town, TN': '1600000US4757480',
                 'Portland city, TN': '1600000US4760280',
                 'Pleasant View city, TN': '1600000US4759560',
                 'Ridgetop city, TN': '1600000US4763140',
                 'Berry Hill city, TN': '1600000US4705140',
                 'Brentwood city, TN': '1600000US4708280',
                 'Burns town, TN': '1600000US4709880',
                 'Hendersonville city, TN': '1600000US4733280',
                 'Kingston Springs town, TN': '1600000US4739660',
                 'Lafayette city, TN': '1600000US4740160',
                 'La Vergne city, TN': '1600000US4741200',
                 'Lebanon city, TN': '1600000US4741520',
                 'McEwen city, TN': '1600000US4744840',
                 'Millersville city, TN': '1600000US4748980',
                 'Mitchellville city, TN': '1600000US4749460',
                 'Mount Juliet city, TN': '1600000US4750780',
                 'Mount Pleasant city, TN': '1600000US4751080',
                 'Murfreesboro city, TN': '1600000US4751560',
                 'Nashville-Davidson metropolitan government (balance), TN': '1600000US4752006',
                 'New Johnsonville city, TN': '1600000US4752820',
                 'Vanleer town, TN': '1600000US4776860',
                 'Watertown city, TN': '1600000US4778320',
                 'Waverly city, TN': '1600000US4778560',
                 'Westmoreland town, TN': '1600000US4779420',
                 'White Bluff town, TN': '1600000US4779980',
                 'White House city, TN': '1600000US4780200',
                 'Eagleville city, TN': '1600000US4722360',
                 'Erin city, TN': '1600000US4724320',
                 'Fairview city, TN': '1600000US4725440',
                 'Forest Hills city, TN': '1600000US4727020',
                 'Franklin city, TN': '1600000US4727740',
                 'Gallatin city, TN': '1600000US4728540',
                 'Goodlettsville city, TN': '1600000US4729920',
                 'Greenbrier town, TN': '1600000US4730960',
                 'Cedar Hill city, TN': '1600000US4711980',
                 'Charlotte town, TN': '1600000US4713080',
                 'Clarksville city, TN': '1600000US4715160',
                 'Coopertown town, TN': '1600000US4716980',
                 'Columbia city, TN': '1600000US4716540',
                 'Cumberland City town, TN': '1600000US4718820',
                 'Cross Plains city, TN': '1600000US4718420',
                 'Dover city, TN': '1600000US4721400',
                 'Smyrna town, TN': '1600000US4769420',
                 'Slayden town, TN': '1600000US4769080',
                 'Springfield city, TN': '1600000US4770500',
                 'Spring Hill city, TN': '1600000US4770580',
                 'Tennessee Ridge town, TN': '1600000US4773460',
                 "Thompson's Station town, TN": '1600000US4773900',
                 'Dickson city, TN': '1600000US4720620',
                 'Franklin city, KY': '1600000US2128918',
                 'Scottsville city, KY': '1600000US2169114',
                 'Tennessee (47)': '0400000US47',
                 'Cheatham County, Tennessee (47021)': '0500000US47021',
                 'Davidson County, Tennessee (47037)': '0500000US47037',
                 'Dickson County, Tennessee (47043)': '0500000US47043',
                 'Houston County, Tennessee (47083)': '0500000US47083',
                 'Humphreys County, Tennessee (47085)': '0500000US47085',
                 'Maury County, Tennessee (47119)': '0500000US47119',
                 'Montgomery County, Tennessee (47125)': '0500000US47125',
                 'Robertson County, Tennessee (47147)': '0500000US47147',
                 'Rutherford County, Tennessee (47149)': '0500000US47149',
                 'Stewart County, Tennessee (47161)': '0500000US47161',
                 'Sumner County, Tennessee (47165)': '0500000US47165',
                 'Trousdale County, Tennessee (47169)': '0500000US47169',
                 'Williamson County, Tennessee (47187)': '0500000US47187',
                 'Wilson County, Tennessee (47189)': '0500000US47189'
}

#list of FIPS codes
GNRC = ['161', #Stewart
       '125', #Montgomery
       '083', #Houston
       '085', #Humphreys
       '043', #Dickson
       '021', #Cheatham
       '147', #Robertson
       '165', #Sumner
       '037', #Davidson
       '189', #Wilson
       '169', #Trousdale
       '187', #Williamson
       '149', #Rutherford
       '119'] #Maury
      #list of FIPS codes
GNRCFULLFIPS = ['47161', #Stewart
        '47125', #Montgomery
        '47083', #Houston
        '47085', #Humphreys
        '47043', #Dickson
        '47021', #Cheatham
        '47147', #Robertson
        '47165', #Sumner
        '47037', #Davidson
        '47189', #Wilson
        '47169', #Trousdale
        '47187', #Williamson
        '47149', #Rutherford
        '47119'] #Maury
KY = ['003', #Allen
      '213'] #Simpson
KYFULLFIPS = ['21003', #Allen
      '21213'] #Simpson
censusplaces = ['1600000US4700200', #Adams city, Tennessee: Robertson
          '1600000US4702180', #Ashland City town, Tennessee: Cheatham
          '1600000US4704620', #Belle Meade city, Tennessee: Davidson
          '1600000US4705140', #Berry Hill city, Tennessee: Davidson
          '1600000US4708280', #Brentwood city, Tennessee: Williamson
          '1600000US4709880', #Burns town, Tennessee: Dickson
          '1600000US4711980', #Cedar Hill city, Tennessee: Robertson
          '1600000US4713080', #Charlotte town, Tennessee: Dickson
          '1600000US4715160', #Clarksville city, Tennessee: Montgomery
          '1600000US4716540', #Columbia city, Tennessee: Maury
          '1600000US4716980', #Coopertown town, Tennessee: Robertson
          '1600000US4718420', #Cross Plains city, Tennessee: Robertson
          '1600000US4718820', #Cumberland City town, Tennessee: Stewart
          '1600000US4720620', #Dickson city, Tennessee: Dickson
          '1600000US4721400', #Dover city, Tennessee: Stewart
          '1600000US4722360', #Eagleville city, Tennessee: Rutherford
          '1600000US4724320', #Erin city, Tennessee: Houston
          '1600000US4725440', #Fairview city, Tennessee: Williamson
          '1600000US4727020', #Forest Hills city, Tennessee: Davidson
          '1600000US4727740', #Franklin city, Tennessee: Williamson
          '1600000US4728540', #Gallatin city, Tennessee: Sumner
          '1600000US4729920', #Goodlettsville city, Tennessee: Davidson/Sumner
          '1600000US4730960', #Greenbrier town, Tennessee: Robertson
          '1600000US4733280', #Hendersonville city, Tennessee: Sumner
          '1600000US4739660', #Kingston Springs town, Tennessee: Cheatham
          '1600000US4741200', #La Vergne city, Tennessee: Rutherford
          '1600000US4740160', #La Vergne city, Tennessee: Macon
          '1600000US4741520', #Lebanon city, Tennessee: Wilson
          '1600000US4744840', #McEwen city, Tennessee: Humphreys
          '1600000US4748980', #Millersville city, Tennessee: Robertson/Sumner
          '1600000US4749460', #Mitchellville city, Tennessee: Sumner
          '1600000US4750780', #Mount Juliet city, Tennessee: Wilson
          '1600000US4751080', #Mount Pleasant city, Tennessee: Maury
          '1600000US4751560', #Murfreesboro city, Tennessee: Rutherford
          '1600000US4752006', #Nashville-Davidson metropolitan government (balance): Davidson
          '1600000US4752820', #New Johnsonville city, Tennessee: Humphreys
          '1600000US4753460', #Nolensville town, Tennessee: Williamson
          '1600000US4754780', #Oak Hill city, Tennessee: Davidson
          '1600000US4757480', #Pegram town, Tennessee: Cheatham
          '1600000US4759560', #Pleasant View city, Tennessee: Cheatham
          '1600000US4760280', #Portland city, Tennessee: Robertson/Sumner
          '1600000US4763140', #Ridgetop city, Tennessee: Davidson/Robertson
          '1600000US4769080', #Slayden town, Tennessee: Dickson
          '1600000US4769420', #Smyrna town, Tennessee: Rutherford
          '1600000US4770580', #Spring Hill city, Tennessee: Maury/Williamson
          '1600000US4770500', #Springfield city, Tennessee: Robertson
          '1600000US4773460', #Tennessee Ridge town, Tennessee: Houston/Stewart
          '1600000US4773900', #Thompson's Station town, Tennessee: Williamson
          '1600000US4776860', #Vanleer town, Tennessee: Dickson
          '1600000US4778320', #Watertown city, Tennessee: Wilson
          '1600000US4778560', #Waverly city, Tennessee: Humphreys
          '1600000US4779420', #Westmoreland town, Tennessee: Sumner
          '1600000US4779980', #White Bluff town, Tennessee: Dickson
          '1600000US4780200', #White House city, Tennessee: Robertson/Sumner
          '1600000US2128918', #Franklin city, Kentucky:
          '1600000US2169114'] #Scottsville city, Kentucky
shortkyplaces = ['28918', #Franklin city, Kentucky:
          '69114'#Scottsville city, Kentucky
          ]
medkyplaces = ['2128918', #Franklin city, Kentucky:
          '2169114'#Scottsville city, Kentucky
]
shorttnplaces = ['00200', #Adams city, Tennessee: Robertson
          '02180', #Ashland City town, Tennessee: Cheatham
          '04620', #Belle Meade city, Tennessee: Davidson
          '05140', #Berry Hill city, Tennessee: Davidson
          '08280', #Brentwood city, Tennessee: Williamson
          '09880', #Burns town, Tennessee: Dickson
          '11980', #Cedar Hill city, Tennessee: Robertson
          '13080', #Charlotte town, Tennessee: Dickson
          '15160', #Clarksville city, Tennessee: Montgomery
          '16540', #Columbia city, Tennessee: Maury
          '16980', #Coopertown town, Tennessee: Robertson
          '18420', #Cross Plains city, Tennessee: Robertson
          '18820', #Cumberland City town, Tennessee: Stewart
          '20620', #Dickson city, Tennessee: Dickson
          '21400', #Dover city, Tennessee: Stewart
          '22360', #Eagleville city, Tennessee: Rutherford
          '24320', #Erin city, Tennessee: Houston
          '25440', #Fairview city, Tennessee: Williamson
          '27020', #Forest Hills city, Tennessee: Davidson
          '27740', #Franklin city, Tennessee: Williamson
          '28540', #Gallatin city, Tennessee: Sumner
          '29920', #Goodlettsville city, Tennessee: Davidson/Sumner
          '30960', #Greenbrier town, Tennessee: Robertson
          '33280', #Hendersonville city, Tennessee: Sumner
          '39660', #Kingston Springs town, Tennessee: Cheatham
          '41200', #La Vergne city, Tennessee: Rutherford
          '40160', #La Vergne city, Tennessee: Macon
          '41520', #Lebanon city, Tennessee: Wilson
          '44840', #McEwen city, Tennessee: Humphreys
          '48980', #Millersville city, Tennessee: Robertson/Sumner
          '49460', #Mitchellville city, Tennessee: Sumner
          '50780', #Mount Juliet city, Tennessee: Wilson
          '51080', #Mount Pleasant city, Tennessee: Maury
          '51560', #Murfreesboro city, Tennessee: Rutherford
          '52006', #Nashville-Davidson metropolitan government (balance): Davidson
          '52820', #New Johnsonville city, Tennessee: Humphreys
          '53460', #Nolensville town, Tennessee: Williamson
          '54780', #Oak Hill city, Tennessee: Davidson
          '57480', #Pegram town, Tennessee: Cheatham
          '59560', #Pleasant View city, Tennessee: Cheatham
          '60280', #Portland city, Tennessee: Robertson/Sumner
          '63140', #Ridgetop city, Tennessee: Davidson/Robertson
          '69080', #Slayden town, Tennessee: Dickson
          '69420', #Smyrna town, Tennessee: Rutherford
          '70580', #Spring Hill city, Tennessee: Maury/Williamson
          '70500', #Springfield city, Tennessee: Robertson
          '73460', #Tennessee Ridge town, Tennessee: Houston/Stewart
          '73900', #Thompson's Station town, Tennessee: Williamson
          '76860', #Vanleer town, Tennessee: Dickson
          '78320', #Watertown city, Tennessee: Wilson
          '78560', #Waverly city, Tennessee: Humphreys
          '79420', #Westmoreland town, Tennessee: Sumner
          '79980', #White Bluff town, Tennessee: Dickson
          '80200'] #White House city, Tennessee: Robertson/Sumner
medtnplaces = ['4700200', #Adams city, Tennessee: Robertson
          '4702180', #Ashland City town, Tennessee: Cheatham
          '4704620', #Belle Meade city, Tennessee: Davidson
          '4705140', #Berry Hill city, Tennessee: Davidson
          '4708280', #Brentwood city, Tennessee: Williamson
          '4709880', #Burns town, Tennessee: Dickson
          '4711980', #Cedar Hill city, Tennessee: Robertson
          '4713080', #Charlotte town, Tennessee: Dickson
          '4715160', #Clarksville city, Tennessee: Montgomery
          '4716540', #Columbia city, Tennessee: Maury
          '4716980', #Coopertown town, Tennessee: Robertson
          '4718420', #Cross Plains city, Tennessee: Robertson
          '4718820', #Cumberland City town, Tennessee: Stewart
          '4720620', #Dickson city, Tennessee: Dickson
          '4721400', #Dover city, Tennessee: Stewart
          '4722360', #Eagleville city, Tennessee: Rutherford
          '4724320', #Erin city, Tennessee: Houston
          '4725440', #Fairview city, Tennessee: Williamson
          '4727020', #Forest Hills city, Tennessee: Davidson
          '4727740', #Franklin city, Tennessee: Williamson
          '4728540', #Gallatin city, Tennessee: Sumner
          '4729920', #Goodlettsville city, Tennessee: Davidson/Sumner
          '4730960', #Greenbrier town, Tennessee: Robertson
          '4733280', #Hendersonville city, Tennessee: Sumner
          '4739660', #Kingston Springs town, Tennessee: Cheatham
          '4741200', #La Vergne city, Tennessee: Rutherford
          '4740160', #La Vergne city, Tennessee: Macon
          '4741520', #Lebanon city, Tennessee: Wilson
          '4744840', #McEwen city, Tennessee: Humphreys
          '4748980', #Millersville city, Tennessee: Robertson/Sumner
          '4749460', #Mitchellville city, Tennessee: Sumner
          '4750780', #Mount Juliet city, Tennessee: Wilson
          '4751080', #Mount Pleasant city, Tennessee: Maury
          '4751560', #Murfreesboro city, Tennessee: Rutherford
          '4752006', #Nashville-Davidson metropolitan government (balance): Davidson
          '4752820', #New Johnsonville city, Tennessee: Humphreys
          '4753460', #Nolensville town, Tennessee: Williamson
          '4754780', #Oak Hill city, Tennessee: Davidson
          '4757480', #Pegram town, Tennessee: Cheatham
          '4759560', #Pleasant View city, Tennessee: Cheatham
          '4760280', #Portland city, Tennessee: Robertson/Sumner
          '4763140', #Ridgetop city, Tennessee: Davidson/Robertson
          '4769080', #Slayden town, Tennessee: Dickson
          '4769420', #Smyrna town, Tennessee: Rutherford
          '4770580', #Spring Hill city, Tennessee: Maury/Williamson
          '4770500', #Springfield city, Tennessee: Robertson
          '4773460', #Tennessee Ridge town, Tennessee: Houston/Stewart
          '4773900', #Thompson's Station town, Tennessee: Williamson
          '4776860', #Vanleer town, Tennessee: Dickson
          '4778320', #Watertown city, Tennessee: Wilson
          '4778560', #Waverly city, Tennessee: Humphreys
          '4779420', #Westmoreland town, Tennessee: Sumner
          '4779980', #White Bluff town, Tennessee: Dickson
          '4780200'] #White House city, Tennessee: Robertson/Sumner
