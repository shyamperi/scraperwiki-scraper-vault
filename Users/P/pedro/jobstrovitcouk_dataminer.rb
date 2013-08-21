# encoding: utf-8

# Trovit.co.uk premium ads dataminer

require 'open-uri'
require 'nokogiri'
require 'net/http'
require 'ostruct'
require 'mechanize'
queries=[
'Accountants',
'Actors',
'Actuaries',
'Acupuncturists',
'Acute+Care+Nurses',
'Adapted+Physical+Education+Specialists',
'Adhesive+Bonding+Machine+Operators+and+Tenders',
'Administrative+Law+Judges,+Adjudicators,+and+Hearing+Officers',
'Administrative+Services+Managers',
'Adult+Basic+and+Secondary+Education+and+Literacy+Teachers+and+Instructors',
'Advanced+Practice+Psychiatric+Nurses',
'Advertising+and+Promotions+Managers',
'Advertising+Sales+Agents',
'Aerospace+Engineering+and+Operations+Technicians',
'Aerospace+Engineers',
'Agents+and+Business+Managers+of+Artists,+Performers,+and+Athletes',
'Agricultural+Engineers',
'Agricultural+Equipment+Operators',
'Agricultural+Inspectors',
'Agricultural+Sciences+Teachers,+Postsecondary',
'Agricultural+Technicians',
'Aircraft+Cargo+Handling+Supervisors',
'Aircraft+Mechanics+and+Service+Technicians',
'Aircraft+Structure,+Surfaces,+Rigging,+and+Systems+Assemblers',
'Airfield+Operations+Specialists',
'Airline+Pilots,+Copilots,+and+Flight+Engineers',
'Air+Traffic+Controllers',
'Allergists+and+Immunologists',
'Ambulance+Drivers+and+Attendants,+Except+Emergency+Medical+Technicians',
'Amusement+and+Recreation+Attendants',
'Anesthesiologist+Assistants',
'Anesthesiologists',
'Animal+Breeders',
'Animal+Control+Workers',
'Animal+Scientists',
'Animal+Trainers',
'Anthropologists',
'Anthropology+and+Archeology+Teachers,+Postsecondary',
'Appraisers,+Real+Estate',
'Aquacultural+Managers',
'Arbitrators,+Mediators,+and+Conciliators',
'Architects,+Except+Landscape+and+Naval',
'Architectural+and+Engineering+Managers',
'Architectural+Drafters',
'Architecture+Teachers,+Postsecondary',
'Archivists',
'Area,+Ethnic,+and+Cultural+Studies+Teachers,+Postsecondary',
'Art+Directors',
'Art,+Drama,+and+Music+Teachers,+Postsecondary',
'Assessors',
'Astronomer',
'Athletes+and+Sports+Competitors',
'Athletic+Trainers',
'Atmospheric+and+Space+Scientists',
'Atmospheric,+Earth,+Marine,+and+Space+Sciences+Teachers,+Postsecondary',
'Audio+and+Video+Equipment+Technicians',
'Audiologists',
'Audio-Visual+and+Multimedia+Collections+Specialists',
'Auditors',
'Automotive+and+Watercraft+Service+Attendants',
'Automotive+Body+and+Related+Repairers',
'Automotive+Glass+Installers+and+Repairers',
'Automotive+Master+Mechanics',
'Automotive+Specialty+Technicians',
'Aviation+Inspectors',
'Avionics+Technicians',
'Baggage+Porters+and+Bellhops',
'Bailiffs',
'Bakers',
'Barbers',
'Bartenders',
'Bicycle+Repairers',
'Bill+and+Account+Collectors',
'Billing,+Cost,+and+Rate+Clerks',
'Biochemical+Engineers',
'Biochemists+and+Biophysicists',
'Bioinformatics+Scientists',
'Biological+Science+Teachers,+Postsecondary',
'Biological+Technicians',
'Biologist',
'Biomass+Plant+Technicians',
'Biomass+Power+Plant+Managers',
'Biomedical+Engineers',
'Biostatisticians',
'Boilermakers',
'Bookkeeping,+Accounting,+and+Auditing+Clerks',
'Bridge+and+Lock+Tenders',
'Broadcast+News+Analysts',
'Broadcast+Technicians',
'Brokerage+Clerks',
'Budget+Analysts',
'Bus+and+Truck+Mechanics+and+Diesel+Engine+Specialists',
'Bus+Drivers,+School+or+Special+Client',
'Bus+Drivers,+Transit+and+Intercity',
'Business+Continuity+Planners',
'Business+Intelligence+Analysts',
'Business+Teachers,+Postsecondary',
'Butchers+and+Meat+Cutters',
'Buyers+and+Purchasing+Agents,+Farm+Products',
'Cabinetmakers+and+Bench+Carpenters',
'Camera+and+Photographic+Equipment+Repairers',
'Camera+Operators,+Television,+Video,+and+Motion+Picture',
'Cardiovascular+Technologists+and+Technicians',
'Career/Technical+Education+Teachers,+Middle+School',
'Career/Technical+Education+Teachers,+Secondary+School',
'Cargo+and+Freight+Agents',
'Carpet+Installers',
'Cashiers',
'Cement+Masons+and+Concrete+Finishers',
'Chefs+and+Head+Cooks',
'Chemical+Engineers',
'Chemical+Equipment+Operators+and+Tenders',
'Chemical+Plant+and+System+Operators',
'Chemical+Technicians',
'Chemistry+Teachers,+Postsecondary',
'Chemists',
'Chief+Executives',
'Childcare+Workers',
'Child,+Family,+and+School+Social+Workers',
'Chiropractors',
'Choreographers',
'City+and+Regional+Planning+Aides',
'Civil+Drafters',
'Civil+Engineering+Technicians',
'Civil+Engineers',
'Claims+Examiners,+Property+and+Casualty+Insurance',
'Cleaners+of+Vehicles+and+Equipment',
'Cleaning,+Washing,+and+Metal+Pickling+Equipment+Operators+and+Tenders',
'Clergy',
'Clinical+Data+Managers',
'Clinical+Nurse+Specialists',
'Clinical+Psychologists',
'Clinical+Research+Coordinators',
'Coaches+and+Scouts',
'Coating,+Painting,+and+Spraying+Machine+Setters,+Operators,+and+Tenders',
'Coil+Winders,+Tapers,+and+Finishers',
'Coin,+Vending,+and+Amusement+Machine+Servicers+and+Repairers',
'Combined+Food+Preparation+and+Serving+Workers,+Including+Fast+Food',
'Commercial+and+Industrial+Designers',
'Commercial+Divers',
'Commercial+Pilots',
'Communications+Teachers,+Postsecondary',
'Compensation+and+Benefits+Managers',
'Compensation,+Benefits,+and+Job+Analysis+Specialists',
'Compliance+Managers',
'Computer+and+Information+Research+Scientists',
'Computer+and+Information+Systems+Managers',
'Computer,+Automated+Teller,+and+Office+Machine+Repairers',
'Computer-Controlled+Machine+Tool+Operators,+Metal+and+Plastic',
'Computer+Hardware+Engineers',
'Computer+Network+Architects',
'Computer+Numerically+Controlled+Machine+Tool+Programmers,+Metal+and+Plastic',
'Computer+Operators',
'Computer+Programmers',
'Computer+Science+Teachers,+Postsecondary',
'Computer+Systems+Analysts',
'Computer+Systems+Engineers/Architects',
'Computer+User+Support+Specialists',
'Concierges',
'Construction+and+Building+Inspectors',
'Construction+Carpenters',
'Construction+Laborers',
'Construction+Managers',
'Continuous+Mining+Machine+Operators',
'Control+and+Valve+Installers+and+Repairers,+Except+Mechanical+Door',
'Conveyor+Operators+and+Tenders',
'Cooks,+Fast+Food',
'Cooks,+Institution+and+Cafeteria',
'Cooks,+Private+Household',
'Cooks,+Restaurant',
'Cooks,+Short+Order',
'Cooling+and+Freezing+Equipment+Operators+and+Tenders',
'Copy+Writers',
'Coroners',
'Correctional+Officers+and+Jailers',
'Correspondence+Clerks',
'Cost+Estimators',
'Costume+Attendants',
'Counseling+Psychologists',
'Counter+and+Rental+Clerks',
'Counter+Attendants,+Cafeteria,+Food+Concession,+and+Coffee+Shop',
'Couriers+and+Messengers',
'Court+Clerks',
'Court+Reporters',
'Craft+Artists',
'Crane+and+Tower+Operators',
'Credit+Analysts',
'Credit+Authorizers',
'Credit+Checkers',
'Criminal+Investigators+and+Special+Agents',
'Criminal+Justice+and+Law+Enforcement+Teachers,+Postsecondary',
'Critical+Care+Nurses',
'Crossing+Guards',
'Crushing,+Grinding,+and+Polishing+Machine+Setters,+Operators,+and+Tenders',
'Curators',
'Customer+Service+Representatives',
'Customs+Brokers',
'Cutters+and+Trimmers,+Hand',
'Cutting+and+Slicing+Machine+Setters,+Operators,+and+Tenders',
'Cutting,+Punching,+and+Press+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Cytogenetic+Technologists',
'Dancers',
'Database+Administrators',
'Data+Entry+Keyers',
'Demonstrators+and+Product+Promoters',
'Dental+Assistants',
'Dental+Hygienists',
'Dental+Laboratory+Technicians',
'Dentists,+General',
'Dermatologists',
'Derrick+Operators,+Oil+and+Gas',
'Desktop+Publishers',
'Diagnostic+Medical+Sonographers',
'Dietetic+Technicians',
'Dietitians+and+Nutritionists',
'Dining+Room+and+Cafeteria+Attendants+and+Bartender+Helpers',
'Directors,+Religious+Activities+and+Education',
'Directors-+Stage,+Motion+Pictures,+Television,+and+Radio',
'Dishwashers',
'Dispatchers,+Except+Police,+Fire,+and+Ambulance',
'Door-To-Door+Sales+Workers,+News+and+Street+Vendors,+and+Related+Workers',
'Dredge+Operators',
'Drilling+and+Boring+Machine+Tool+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Driver/Sales+Workers',
'Drywall+and+Ceiling+Tile+Installers',
'Earth+Drillers,+Except+Oil+and+Gas',
'Economics+Teachers,+Postsecondary',
'Economists',
'Editors',
'Education+Administrators,+Elementary+and+Secondary+School',
'Education+Administrators,+Postsecondary',
'Education+Administrators,+Preschool+and+Childcare+Center/Program',
'Educational,+Guidance,+School,+and+Vocational+Counselors',
'Education+Teachers,+Postsecondary',
'Electrical+and+Electronic+Equipment+Assemblers',
'Electrical+and+Electronics+Installers+and+Repairers,+Transportation+Equipment',
'Electrical+and+Electronics+Repairers,+Commercial+and+Industrial+Equipment',
'Electrical+and+Electronics+Repairers,+Powerhouse,+Substation,+and+Relay',
'Electrical+Drafters',
'Electrical+Engineering+Technicians',
'Electrical+Engineering+Technologists',
'Electrical+Engineers',
'Electrical+Power-Line+Installers+and+Repairers',
'Electricians',
'Electric+Motor,+Power+Tool,+and+Related+Repairers',
'Electromechanical+Engineering+Technologists',
'Electromechanical+Equipment+Assemblers',
'Electro-Mechanical+Technicians',
'Electronic+Drafters',
'Electronic+Equipment+Installers+and+Repairers,+Motor+Vehicles',
'Electronic+Home+Entertainment+Equipment+Installers+and+Repairers',
'Electronics+Engineering+Technicians',
'Electronics+Engineering+Technologists',
'Electronics+Engineers,+Except+Computer',
'Elementary+School+Teachers,+Except+Special+Education',
'Elevator+Installers+and+Repairers',
'Eligibility+Interviewers,+Government+Programs',
'Emergency+Management+Directors',
'Emergency+Medical+Technicians+and+Paramedics',
'Endoscopy+Technicians',
'Energy+Auditors',
'Energy+Engineers',
'Engine+and+Other+Machine+Assemblers',
'Engineering+Teachers,+Postsecondary',
'English+Language+and+Literature+Teachers,+Postsecondary',
'Environmental+Compliance+Inspectors',
'Environmental+Economists',
'Environmental+Engineering+Technicians',
'Environmental+Engineers',
'Environmental+Science+and+Protection+Technicians,+Including+Health',
'Environmental+Science+Teachers,+Postsecondary',
'Environmental+Scientists+and+Specialists,+Including+Health',
'Epidemiologists',
'Equal+Opportunity+Representatives+and+Officers',
'Etchers+and+Engravers',
'Excavating+and+Loading+Machine+and+Dragline+Operators',
'Executive+Secretaries+and+Executive+Administrative+Assistants',
'Explosives+Workers,+Ordnance+Handling+Experts,+and+Blasters',
'Extruding+and+Drawing+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Extruding+and+Forming+Machine+Setters,+Operators,+and+Tenders,+Synthetic+and+Glass+Fibers',
'Extruding,+Forming,+Pressing,+and+Compacting+Machine+Setters,+Operators,+and+Tenders',
'Fabric+and+Apparel+Patternmakers',
'Fabric+Menders,+Except+Garment',
'Fallers',
'Family+and+General+Practitioners',
'Farm+and+Home+Management+Advisors',
'Farm+Equipment+Mechanics+and+Service+Technicians',
'Farm+Labor+Contractors',
'Farmworkers+and+Laborers,+Crop',
'Farmworkers,+Farm,+Ranch,+and+Aquacultural+Animals',
'Fashion+Designers',
'Fence+Erectors',
'Fiberglass+Laminators+and+Fabricators',
'File+Clerks',
'Film+and+Video+Editors',
'Financial+Analysts',
'Financial+Examiners',
'Financial+Managers,+Branch+or+Department',
'Fine+Artists,+Including+Painters,+Sculptors,+and+Illustrators',
'Fire+Inspectors',
'Fire+Investigators',
'Fire-Prevention+and+Protection+Engineers',
'First-Line+Supervisors+of+Agricultural+Crop+and+Horticultural+Workers',
'First-Line+Supervisors+of+Animal+Husbandry+and+Animal+Care+Workers',
'First-Line+Supervisors+of+Aquacultural+Workers',
'First-Line+Supervisors+of+Construction+Trades+and+Extraction+Workers',
'First-Line+Supervisors+of+Correctional+Officers',
'First-Line+Supervisors+of+Food+Preparation+and+Serving+Workers',
'First-Line+Supervisors+of+Helpers,+Laborers,+and+Material+Movers,+Hand',
'First-Line+Supervisors+of+Housekeeping+and+Janitorial+Workers',
'First-Line+Supervisors+of+Landscaping,+Lawn+Service,+and+Groundskeeping+Workers',
'First-Line+Supervisors+of+Logging+Workers',
'First-Line+Supervisors+of+Mechanics,+Installers,+and+Repairers',
'First-Line+Supervisors+of+Non-Retail+Sales+Workers',
'First-Line+Supervisors+of+Office+and+Administrative+Support+Workers',
'First-Line+Supervisors+of+Personal+Service+Workers',
'First-Line+Supervisors+of+Police+and+Detectives',
'First-Line+Supervisors+of+Production+and+Operating+Workers',
'First-Line+Supervisors+of+Retail+Sales+Workers',
'First-Line+Supervisors+of+Transportation+and+Material-Moving+Machine+and+Vehicle+Operators',
'Fish+and+Game+Wardens',
'Fishers+and+Related+Fishing+Workers',
'Fitness+Trainers+and+Aerobics+Instructors',
'Flight+Attendants',
'Floor+Layers,+Except+Carpet,+Wood,+and+Hard+Tiles',
'Floor+Sanders+and+Finishers',
'Floral+Designers',
'Food+and+Tobacco+Roasting,+Baking,+and+Drying+Machine+Operators+and+Tenders',
'Food+Batchmakers',
'Food+Cooking+Machine+Operators+and+Tenders',
'Food+Preparation+Workers',
'Food+Science+Technicians',
'Food+Scientists+and+Technologists',
'Food+Servers,+Nonrestaurant',
'Food+Service+Managers',
'Foreign+Language+and+Literature+Teachers,+Postsecondary',
'Forensic+Science+Technicians',
'Forest+and+Conservation+Technicians',
'Forest+and+Conservation+Workers',
'Foresters',
'Forest+Firefighters',
'Forest+Fire+Fighting+and+Prevention+Supervisors',
'Forest+Fire+Inspectors+and+Prevention+Specialists',
'Forestry+and+Conservation+Science+Teachers,+Postsecondary',
'Forging+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Foundry+Mold+and+Coremakers',
'Fraud+Examiners,+Investigators+and+Analysts',
'Freight+and+Cargo+Inspectors',
'Funeral+Attendants',
'Furnace,+Kiln,+Oven,+Drier,+and+Kettle+Operators+and+Tenders',
'Furniture+Finishers',
'Gaming+and+Sports+Book+Writers+and+Runners',
'Gaming+Cage+Workers',
'Gaming+Change+Persons+and+Booth+Cashiers',
'Gaming+Dealers',
'Gaming+Managers',
'Gaming+Supervisors',
'Gaming+Surveillance+Officers+and+Gaming+Investigators',
'Gas+Compressor+and+Gas+Pumping+Station+Operators',
'Gas+Plant+Operators',
'Gem+and+Diamond+Workers',
'General+and+Operations+Managers',
'Genetic+Counselors',
'Geneticists',
'Geodetic+Surveyors',
'Geographers',
'Geographic+Information+Systems+Technicians',
'Geography+Teachers,+Postsecondary',
'Geological+Sample+Test+Technicians',
'Geophysical+Data+Technicians',
'Geoscientists,+Except+Hydrologists+and+Geographers',
'Geospatial+Information+Scientists+and+Technologists',
'Geothermal+Production+Managers',
'Geothermal+Technicians',
'Glass+Blowers,+Molders,+Benders,+and+Finishers',
'Glaziers',
'Government+Property+Inspectors+and+Investigators',
'Graders+and+Sorters,+Agricultural+Products',
'Graduate+Teaching+Assistants',
'Graphic+Designers',
'Hairdressers,+Hairstylists,+and+Cosmetologists',
'Hazardous+Materials+Removal+Workers',
'Healthcare+Social+Workers',
'Health+Educators',
'Health+Specialties+Teachers,+Postsecondary',
'Hearing+Aid+Specialists',
'Heating+and+Air+Conditioning+Mechanics+and+Installers',
'Heat+Treating+Equipment+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Heavy+and+Tractor-Trailer+Truck+Drivers',
'Helpers--Carpenters',
'Helpers--Electricians',
'Helpers--Extraction+Workers',
'Helpers--Installation,+Maintenance,+and+Repair+Workers',
'Helpers--Painters,+Paperhangers,+Plasterers,+and+Stucco+Masons',
'Helpers--Pipelayers,+Plumbers,+Pipefitters,+and+Steamfitters',
'Helpers--Production+Workers',
'Helpers--Roofers',
'Highway+Maintenance+Workers',
'Historians',
'History+Teachers,+Postsecondary',
'Histotechnologists+and+Histologic+Technicians',
'Hoist+and+Winch+Operators',
'Home+Appliance+Repairers',
'Home+Economics+Teachers,+Postsecondary',
'Home+Health+Aides',
'Hospitalists',
'Hosts+and+Hostesses,+Restaurant,+Lounge,+and+Coffee+Shop',
'Hotel,+Motel,+and+Resort+Desk+Clerks',
'Human+Factors+Engineers+and+Ergonomists',
'Human+Resources+Assistants,+Except+Payroll+and+Timekeeping',
'Human+Resources+Managers',
'Human+Resources+Specialists',
'Hunters+and+Trappers',
'Hydrologists',
'Immigration+and+Customs+Inspectors',
'Industrial+Engineering+Technicians',
'Industrial+Engineering+Technologists',
'Industrial+Engineers',
'Industrial+Machinery+Mechanics',
'Industrial-Organizational+Psychologists',
'Industrial+Production+Managers',
'Industrial+Safety+and+Health+Engineers',
'Industrial+Truck+and+Tractor+Operators',
'Informatics+Nurse+Specialists',
'Information+Security+Analysts',
'Information+Technology+Project+Managers',
'Inspectors,+Testers,+Sorters,+Samplers,+and+Weighers',
'Instructional+Coordinators',
'Insulation+Workers,+Floor,+Ceiling,+and+Wall',
'Insulation+Workers,+Mechanical',
'Insurance+Adjusters,+Examiners,+and+Investigators',
'Insurance+Appraisers,+Auto+Damage',
'Insurance+Claims+Clerks',
'Insurance+Policy+Processing+Clerks',
'Insurance+Sales+Agents',
'Insurance+Underwriters',
'Intelligence+Analysts',
'Interior+Designers',
'Internists,+General',
'Interpreters+and+Translators',
'Interviewers,+Except+Eligibility+and+Loan',
'Janitors+and+Cleaners,+Except+Maids+and+Housekeeping+Cleaners',
'Jewelers',
'Judges,+Magistrate+Judges,+and+Magistrates',
'Judicial+Law+Clerks',
'Kindergarten+Teachers,+Except+Special+Education',
'Laborers+and+Freight,+Stock,+and+Material+Movers,+Hand',
'Landscape+Architects',
'Landscaping+and+Groundskeeping+Workers',
'Lathe+and+Turning+Machine+Tool+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Laundry+and+Dry-Cleaning+Workers',
'Law+Teachers,+Postsecondary',
'Lawyers',
'Layout+Workers,+Metal+and+Plastic',
'Legal+Secretaries',
'Legislators',
'Librarians',
'Library+Assistants,+Clerical',
'Library+Science+Teachers,+Postsecondary',
'Library+Technicians',
'License+Clerks',
'Licensed+Practical+and+Licensed+Vocational+Nurses',
'Licensing+Examiners+and+Inspectors',
'Lifeguards,+Ski+Patrol,+and+Other+Recreational+Protective+Service+Workers',
'Light+Truck+or+Delivery+Services+Drivers',
'Loading+Machine+Operators,+Underground+Mining',
'Loan+Counselors',
'Loan+Interviewers+and+Clerks',
'Loan+Officers',
'Locker+Room,+Coatroom,+and+Dressing+Room+Attendants',
'Locksmiths+and+Safe+Repairers',
'Locomotive+Engineers',
'Locomotive+Firers',
'Lodging+Managers',
'Logging+Equipment+Operators',
'Log+Graders+and+Scalers',
'Logisticians',
'Logistics+Analysts',
'Logistics+Engineers',
'Logistics+Managers',
'Loss+Prevention+Managers',
'Low+Vision+Therapists,+Orientation+and+Mobility+Specialists,+and+Vision+Rehabilitation+Therapists',
'Machine+Feeders+and+Offbearers',
'Machinists',
'Magnetic+Resonance+Imaging+Technologists',
'Maids+and+Housekeeping+Cleaners',
'Mail+Clerks+and+Mail+Machine+Operators,+Except+Postal+Service',
'Maintenance+and+Repair+Workers,+General',
'Maintenance+Workers,+Machinery',
'Makeup+Artists,+Theatrical+and+Performance',
'Management+Analysts',
'Manicurists+and+Pedicurists',
'Manufactured+Building+and+Mobile+Home+Installers',
'Manufacturing+Engineering+Technologists',
'Manufacturing+Engineers',
'Manufacturing+Production+Technicians',
'Mapping+Technicians',
'Marine+Architects',
'Marine+Engineers',
'Marketing+Managers',
'Market+Research+Analysts+and+Marketing+Specialists',
'Marking+Clerks',
'Marriage+and+Family+Therapists',
'Massage+Therapists',
'Materials+Engineers',
'Materials+Scientists',
'Mates-+Ship,+Boat,+and+Barge',
'Mathematical+Science+Teachers,+Postsecondary',
'Mathematical+Technicians',
'Mathematicians',
'Meat,+Poultry,+and+Fish+Cutters+and+Trimmers',
'Mechanical+Door+Repairers',
'Mechanical+Drafters',
'Mechanical+Engineering+Technicians',
'Mechanical+Engineering+Technologists',
'Mechanical+Engineers',
'Mechatronics+Engineers',
'Medical+and+Clinical+Laboratory+Technicians',
'Medical+and+Clinical+Laboratory+Technologists',
'Medical+and+Health+Services+Managers',
'Medical+Appliance+Technicians',
'Medical+Assistants',
'Medical+Equipment+Preparers',
'Medical+Equipment+Repairers',
'Medical+Records+and+Health+Information+Technicians',
'Medical+Scientists,+Except+Epidemiologists',
'Medical+Secretaries',
'Medical+Transcriptionists',
'Meeting,+Convention,+and+Event+Planners',
'Mental+Health+and+Substance+Abuse+Social+Workers',
'Mental+Health+Counselors',
'Merchandise+Displayers+and+Window+Trimmers',
'Metal-Refining+Furnace+Operators+and+Tenders',
'Meter+Readers,+Utilities',
'Microbiologists',
'Middle+School+Teachers,+Except+Special+and+Career/Technical+Education',
'Midwives',
'Milling+and+Planing+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Millwrights',
'Mine+Cutting+and+Channeling+Machine+Operators',
'Mine+Shuttle+Car+Operators',
'Mining+and+Geological+Engineers,+Including+Mining+Safety+Engineers',
'Mixing+and+Blending+Machine+Setters,+Operators,+and+Tenders',
'Mobile+Heavy+Equipment+Mechanics,+Except+Engines',
'Model+Makers,+Metal+and+Plastic',
'Model+Makers,+Wood',
'Models',
'Molding+and+Casting+Workers',
'Molding,+Coremaking,+and+Casting+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Molecular+and+Cellular+Biologists',
'Morticians,+Undertakers,+and+Funeral+Directors',
'Motion+Picture+Projectionists',
'Motorboat+Mechanics+and+Service+Technicians',
'Motorboat+Operators',
'Motorcycle+Mechanics',
'Multimedia+Artists+and+Animators',
'Multiple+Machine+Tool+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Municipal+Clerks',
'Municipal+Firefighters',
'Municipal+Fire+Fighting+and+Prevention+Supervisors',
'Museum+Technicians+and+Conservators',
'Musical+Instrument+Repairers+and+Tuners',
'Music+Composers+and+Arrangers',
'Music+Directors',
'Musicians,+Instrumental',
'Nannies',
'Natural+Sciences+Managers',
'Naturopathic+Physicians',
'Network+and+Computer+Systems+Administrators',
'Neurodiagnostic+Technologists',
'Neurologists',
'Neuropsychologists+and+Clinical+Neuropsychologists',
'New+Accounts+Clerks',
'Non-Destructive+Testing+Specialists',
'Nonfarm+Animal+Caretakers',
'Nuclear+Engineers',
'Nuclear+Equipment+Operation+Technicians',
'Nuclear+Medicine+Physicians',
'Nuclear+Medicine+Technologists',
'Nuclear+Monitoring+Technicians',
'Nuclear+Power+Reactor+Operators',
'Nurse+Anesthetists',
'Nurse+Midwives',
'Nurse+Practitioners',
'Nursery+and+Greenhouse+Managers',
'Nursery+Workers',
'Nursing+Instructors+and+Teachers,+Postsecondary',
'Obstetricians+and+Gynecologists',
'Occupational+Health+and+Safety+Specialists',
'Occupational+Health+and+Safety+Technicians',
'Occupational+Therapists',
'Occupational+Therapy+Aides',
'Occupational+Therapy+Assistants',
'Office+Clerks,+General',
'Office+Machine+Operators,+Except+Computer',
'Operating+Engineers+and+Other+Construction+Equipment+Operators',
'Operations+Research+Analysts',
'Ophthalmic+Laboratory+Technicians',
'Ophthalmologists',
'Opticians,+Dispensing',
'Optometrists',
'Oral+and+Maxillofacial+Surgeons',
'Order+Clerks',
'Order+Fillers,+Wholesale+and+Retail+Sales',
'Orthodontists',
'Orthoptists',
'Orthotists+and+Prosthetists',
'Outdoor+Power+Equipment+and+Other+Small+Engine+Mechanics',
'Packaging+and+Filling+Machine+Operators+and+Tenders',
'Packers+and+Packagers,+Hand',
'Painters,+Construction+and+Maintenance',
'Painters,+Transportation+Equipment',
'Painting,+Coating,+and+Decorating+Workers',
'Paper+Goods+Machine+Setters,+Operators,+and+Tenders',
'Paperhangers',
'Paralegals+and+Legal+Assistants',
'Parking+Enforcement+Workers',
'Parking+Lot+Attendants',
'Park+Naturalists',
'Parts+Salespersons',
'Pathologists',
'Patient+Representatives',
'Patternmakers,+Metal+and+Plastic',
'Patternmakers,+Wood',
'Paving,+Surfacing,+and+Tamping+Equipment+Operators',
'Payroll+and+Timekeeping+Clerks',
'Pediatricians,+General',
'Personal+Care+Aides',
'Personal+Financial+Advisors',
'Pest+Control+Workers',
'Pesticide+Handlers,+Sprayers,+and+Applicators,+Vegetation',
'Petroleum+Engineers',
'Petroleum+Pump+System+Operators,+Refinery+Operators,+and+Gaugers',
'Pharmacists',
'Pharmacy+Aides',
'Pharmacy+Technicians',
'Philosophy+and+Religion+Teachers,+Postsecondary',
'Phlebotomists',
'Photographers',
'Photographic+Process+Workers+and+Processing+Machine+Operators',
'Photonics+Engineers',
'Physical+Medicine+and+Rehabilitation+Physicians',
'Physical+Therapist+Aides',
'Physical+Therapist+Assistants',
'Physical+Therapists',
'Physician+Assistants',
'Physicists',
'Physics+Teachers,+Postsecondary',
'Pile-Driver+Operators',
'Pilots,+Ship',
'Pipe+Fitters+and+Steamfitters',
'Pipelayers',
'Plasterers+and+Stucco+Masons',
'Plating+and+Coating+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Plumbers',
'Podiatrists',
'Poets,+Lyricists+and+Creative+Writers',
'Police+Detectives',
'Police,+Fire,+and+Ambulance+Dispatchers',
'Police+Identification+and+Records+Officers',
'Police+Patrol+Officers',
'Political+Science+Teachers,+Postsecondary',
'Political+Scientists',
'Postal+Service+Clerks',
'Postal+Service+Mail+Carriers',
'Postal+Service+Mail+Sorters,+Processors,+and+Processing+Machine+Operators',
'Postmasters+and+Mail+Superintendents',
'Potters,+Manufacturing',
'Pourers+and+Casters,+Metal',
'Power+Distributors+and+Dispatchers',
'Power+Plant+Operators',
'Precious+Metal+Workers',
'Precision+Agriculture+Technicians',
'Prepress+Technicians+and+Workers',
'Preschool+Teachers,+Except+Special+Education',
'Pressers,+Textile,+Garment,+and+Related+Materials',
'Preventive+Medicine+Physicians',
'Print+Binding+and+Finishing+Workers',
'Printing+Press+Operators',
'Private+Detectives+and+Investigators',
'Probation+Officers+and+Correctional+Treatment+Specialists',
'Procurement+Clerks',
'Producers',
'Production,+Planning,+and+Expediting+Clerks',
'Product+Safety+Engineers',
'Program+Directors',
'Proofreaders+and+Copy+Markers',
'Property,+Real+Estate,+and+Community+Association+Managers',
'Prosthodontists',
'Psychiatric+Aides',
'Psychiatric+Technicians',
'Psychiatrists',
'Psychology+Teachers,+Postsecondary',
'Public+Address+System+and+Other+Announcers',
'Public+Relations+and+Fundraising+Managers',
'Public+Relations+Specialists',
'Pump+Operators,+Except+Wellhead+Pumpers',
'Purchasing+Agents,+Except+Wholesale,+Retail,+and+Farm+Products',
'Purchasing+Managers',
'Quality+Control+Analysts',
'Quality+Control+Systems+Managers',
'Radiation+Therapists',
'Radio+and+Television+Announcers',
'Radiologic+Technicians',
'Radiologic+Technologists',
'Radiologists',
'Radio+Mechanics',
'Radio+Operators',
'Rail+Car+Repairers',
'Railroad+Brake,+Signal,+and+Switch+Operators',
'Railroad+Conductors+and+Yardmasters',
'Rail-Track+Laying+and+Maintenance+Equipment+Operators',
'Rail+Yard+Engineers,+Dinkey+Operators,+and+Hostlers',
'Range+Managers',
'Real+Estate+Brokers',
'Real+Estate+Sales+Agents',
'Receptionists+and+Information+Clerks',
'Recreational+Therapists',
'Recreational+Vehicle+Service+Technicians',
'Recreation+and+Fitness+Studies+Teachers,+Postsecondary',
'Recreation+Workers',
'Recycling+and+Reclamation+Workers',
'Refractory+Materials+Repairers,+Except+Brickmasons',
'Refrigeration+Mechanics+and+Installers',
'Refuse+and+Recyclable+Material+Collectors',
'Registered+Nurses',
'Regulatory+Affairs+Managers',
'Regulatory+Affairs+Specialists',
'Rehabilitation+Counselors',
'Reinforcing+Iron+and+Rebar+Workers',
'Remote+Sensing+Scientists+and+Technologists',
'Remote+Sensing+Technicians',
'Reporters+and+Correspondents',
'Reservation+and+Transportation+Ticket+Agents+and+Travel+Clerks',
'Residential+Advisors',
'Respiratory+Therapists',
'Respiratory+Therapy+Technicians',
'Retail+Salespersons',
'Riggers',
'Risk+Management+Specialists',
'Robotics+Engineers',
'Robotics+Technicians',
'Rock+Splitters,+Quarry',
'Rolling+Machine+Setters,+Operators,+and+Tenders,+Metal+and+Plastic',
'Roof+Bolters,+Mining',
'Roofers',
'Rotary+Drill+Operators,+Oil+and+Gas',
'Rough+Carpenters',
'Roustabouts,+Oil+and+Gas',
'Sailors+and+Marine+Oilers',
'Sales+Agents,+Financial+Services',
'Sales+Agents,+Securities+and+Commodities',
'Sales+Engineers',
'Sales+Managers',
'Sales+Representatives,+Wholesale+and+Manufacturing,+Except+Technical+and+Scientific+Products',
'Sales+Representatives,+Wholesale+and+Manufacturing,+Technical+and+Scientific+Products',
'Sawing+Machine+Setters,+Operators,+and+Tenders,+Wood',
'School+Psychologists',
'Secondary+School+Teachers,+Except+Special+and+Career/Technical+Education',
'Secretaries+and+Administrative+Assistants,+Except+Legal,+Medical,+and+Executive',
'Security+and+Fire+Alarm+Systems+Installers',
'Security+Guards',
'Segmental+Pavers',
'Self-Enrichment+Education+Teachers',
'Semiconductor+Processors',
'Separating,+Filtering,+Clarifying,+Precipitating,+and+Still+Machine+Setters,+Operators,+and+Tenders',
'Septic+Tank+Servicers+and+Sewer+Pipe+Cleaners',
'Service+Unit+Operators,+Oil,+Gas,+and+Mining',
'Set+and+Exhibit+Designers',
'Sewers,+Hand',
'Sewing+Machine+Operators',
'Shampooers',
'Sheet+Metal+Workers',
'Sheriffs+and+Deputy+Sheriffs',
'Ship+and+Boat+Captains',
'Ship+Engineers',
'Shipping,+Receiving,+and+Traffic+Clerks',
'Shoe+and+Leather+Workers+and+Repairers',
'Shoe+Machine+Operators+and+Tenders',
'Signal+and+Track+Switch+Repairers',
'Singers',
'Skincare+Specialists',
'Slaughterers+and+Meat+Packers',
'Slot+Supervisors',
'Social+and+Community+Service+Managers',
'Social+and+Human+Service+Assistants',
'Social+Science+Research+Assistants',
'Social+Work+Teachers,+Postsecondary',
'Sociologists',
'Sociology+Teachers,+Postsecondary',
'Software+Developers,+Applications',
'Software+Developers,+Systems+Software',
'Software+Quality+Assurance+Engineers+and+Testers',
'Soil+and+Plant+Scientists',
'Soil+and+Water+Conservationists',
'Solar+Photovoltaic+Installers',
'Solar+Sales+Representatives+and+Assessors',
'Solderers+and+Brazers',
'Sound+Engineering+Technicians',
'Spa+Managers',
'Special+Education+Teachers,+Middle+School',
'Special+Education+Teachers,+Secondary+School',
'Speech-Language+Pathologists',
'Speech-Language+Pathology+Assistants',
'Sports+Medicine+Physicians',
'Statement+Clerks',
'Stationary+Engineers+and+Boiler+Operators',
'Statistical+Assistants',
'Statisticians',
'Stock+Clerks,+Sales+Floor',
'Stock+Clerks-+Stockroom,+Warehouse,+or+Storage+Yard',
'Stone+Cutters+and+Carvers,+Manufacturing',
'Stonemasons',
'Storage+and+Distribution+Managers',
'Structural+Iron+and+Steel+Workers',
'Structural+Metal+Fabricators+and+Fitters',
'Substance+Abuse+and+Behavioral+Disorder+Counselors',
'Subway+and+Streetcar+Operators',
'Supply+Chain+Managers',
'Surgeons',
'Surgical+Technologists',
'Surveying+Technicians',
'Surveyors',
'Survey+Researchers',
'Switchboard+Operators,+Including+Answering+Service',
'Tailors,+Dressmakers,+and+Custom+Sewers',
'Talent+Directors',
'Tank+Car,+Truck,+and+Ship+Loaders',
'Tapers',
'Tax+Examiners+and+Collectors,+and+Revenue+Agents',
'Taxi+Drivers+and+Chauffeurs',
'Tax+Preparers',
'Teacher+Assistants',
'Team+Assemblers',
'Technical+Directors/Managers',
'Technical+Writers',
'Telecommunications+Equipment+Installers+and+Repairers,+Except+Line+Installers',
'Telecommunications+Line+Installers+and+Repairers',
'Telemarketers',
'Telephone+Operators',
'Tellers',
'Terrazzo+Workers+and+Finishers',
'Textile+Bleaching+and+Dyeing+Machine+Operators+and+Tenders',
'Textile+Cutting+Machine+Setters,+Operators,+and+Tenders',
'Textile+Knitting+and+Weaving+Machine+Setters,+Operators,+and+Tenders',
'Textile+Winding,+Twisting,+and+Drawing+Out+Machine+Setters,+Operators,+and+Tenders',
'Tile+and+Marble+Setters',
'Timing+Device+Assemblers+and+Adjusters',
'Tire+Builders',
'Tire+Repairers+and+Changers',
'Title+Examiners,+Abstractors,+and+Searchers',
'Tool+and+Die+Makers',
'Tool+Grinders,+Filers,+and+Sharpeners',
'Tour+Guides+and+Escorts',
'Traffic+Technicians',
'Training+and+Development+Managers',
'Training+and+Development+Specialists',
'Transit+and+Railroad+Police',
'Transportation+Attendants,+Except+Flight+Attendants',
'Transportation+Engineers',
'Transportation+Managers',
'Transportation+Planners',
'Transportation+Security+Screeners',
'Transportation+Vehicle,+Equipment+and+Systems+Inspectors,+Except+Aviation',
'Travel+Agents',
'Travel+Guides',
'Treasurers+and+Controllers',
'Tree+Trimmers+and+Pruners',
'Umpires,+Referees,+and+Other+Sports+Officials',
'Upholsterers',
'Urban+and+Regional+Planners',
'Urologists',
'Ushers,+Lobby+Attendants,+and+Ticket+Takers',
'Validation+Engineers',
'Veterinarians',
'Veterinary+Assistants+and+Laboratory+Animal+Caretakers',
'Veterinary+Technologists+and+Technicians',
'Video+Game+Designers',
'Vocational+Education+Teachers,+Postsecondary',
'Waiters+and+Waitresses',
'Watch+Repairers',
'Water+and+Wastewater+Treatment+Plant+and+System+Operators',
'Water+Resource+Specialists',
'Water/Wastewater+Engineers',
'Weatherization+Installers+and+Technicians',
'Web+Administrators',
'Web+Developers',
'Weighers,+Measurers,+Checkers,+and+Samplers,+Recordkeeping',
'Welders,+Cutters,+and+Welder+Fitters',
'Welding,+Soldering,+and+Brazing+Machine+Setters,+Operators,+and+Tenders',
'Wellhead+Pumpers',
'Wholesale+and+Retail+Buyers,+Except+Farm+Products',
'Wind+Energy+Engineers',
'Woodworking+Machine+Setters,+Operators,+and+Tenders,+Except+Sawing',
'Word+Processors+and+Typists',
'Zoologists+and+Wildlife+Biologists',
'Aberdeen',
'Armagh',
'Bangor',
'Bath',
'Belfast',
'Birmingham',
'Bradford',
'Brighton+and+Hove',
'Bristol',
'Cambridge',
'Canterbury',
'Cardiff',
'Carlisle',
'Chester',
'Chichester',
'City+of+London',
'Coventry',
'Derby',
'Dundee',
'Durham',
'Edinburgh',
'Ely',
'Exeter',
'Glasgow',
'Gloucester',
'Hereford',
'Inverness',
'Kingston+upon+Hull',
'Lancaster',
'Leeds',
'Leicester',
'Lichfield',
'Lincoln',
'Lisburn',
'Liverpool',
'Londonderry',
'Manchester',
'Newcastle+upon+Tyne',
'Newport',
'Newry',
'Norwich',
'Nottingham',
'Oxford',
'Peterborough',
'Plymouth',
'Portsmouth',
'Preston',
'Ripon',
'Salford',
'Salisbury',
'Sheffield',
'Southampton',
'St+Albans',
'St+Davids',
'Stirling',
'Stoke-on-Trent',
'Sunderland',
'Swansea',
'Truro',
'Wakefield',
'Wells',
'Westminster',
'Winchester',
'Wolverhampton',
'Worcester',
'York',
'Engineering+in+Birmingham',
'Engineering+in+Bristol',
'Engineering+in+Colchester',
'Engineering+in+Leicester',
'Finance+in+Bristol',
'Finance+in+Edinburgh',
'Finance+in+London',
'Finance+in+Manchester',
'IT+in+Kent',
'IT+in+Leeds',
'IT+in+London',
'IT+in+Manchester',
'Marketing+in+Manchester',
'Marketing+in+Nottingham',
'Marketing+in+Surrey',
'Marketing+in+West+London',
'Nursing+in+Birmingham',
'Nursing+in+Cardiff',
'Nursing+in+Liverpool',
'Nursing+in+London']
counts = Hash.new(0)
j=0
while j<queries.count
  queryurl='http://jobs.trovit.co.uk/index.php/cod.search_jobs/what_d.'+queries[j]
 # puts queryurl
  doc = Nokogiri::HTML(open(URI::encode(queryurl)))
doc.search("div[@id='wrapper_ppc_top']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")  
    if(cells.count>0)  
    #puts cells.text
    name=cells.text
    data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
   end
end
doc.search("div[@id='wrapper_ppc_bottom']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")   
   # puts cells.text
    if(cells.count>0)  
   name=cells.text
   data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
  end
  end
j=j+1
end
