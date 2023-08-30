# [Regulations.gov](https://www.regulations.gov/) archive

Data scrape and archive of regulations.gov using [v4 API](https://open.gsa.gov/api/regulationsgov/).

Regulations are organized by five document types: `Rule`, `Proposed Rule`, `Notice`, `Other`, and `Supporting & Related Material`. This project only collects documents on the first two types: `Rule` and `Proposed Rule`.

## Artifacts

+ [All documents and comment counts for `Rule` and `Proposed Rule`](artifacts/LISTING_rules_and_posted_rules.csv)


## Data Statistics
|     |     |
|---- |---- |
| Total documents | 132,012    |
| Unique agencies | 252    |
| Unique dockets  | 61,213   |
| Unique FR IDs   | 103,849      |
| Total comments  | 2,396,131  |

## Data ingestion progress
|     |     |
|---- |---- |
| Latest date   | 2023-08-15 |
| Earliest date | 1990-01-10    |
| Fraction of documents scanned for comments  | 0.1601 |

## Top 30 documents with most comments
| docId | comments | Title |
|------|---------:|-------|
| [ED-2021-OCR-0166-0001](https://www.regulations.gov/document/ED-2021-OCR-0166-0001) | 238,987 | Nondiscrimination on the Basis of Sex in Education Programs or Activities Receiving Federal Financial Assistance |
| [CFPB-2016-0025-0001](https://www.regulations.gov/document/CFPB-2016-0025-0001) | 211,885 | Payday, Vehicle Title, and Certain High-Cost Installment Loans |
| [HHS-OS-2018-0008-0001](https://www.regulations.gov/document/HHS-OS-2018-0008-0001) | 204,771 | Compliance with Statutory Program Integrity Requirements |
| [FDA-2021-N-1349-0001](https://www.regulations.gov/document/FDA-2021-N-1349-0001) | 175,299 | Tobacco Product Standard for Menthol in Cigarettes |
| [ED-2022-OCR-0143-0001](https://www.regulations.gov/document/ED-2022-OCR-0143-0001) | 156,158 | Nondiscrimination on the Basis of Sex in Education Programs or Activities Receiving Federal Financial Assistance: Sex-Related Eligibility Criteria for Male and Female Athletic Teams |
| [SSA-2018-0026-0001](https://www.regulations.gov/document/SSA-2018-0026-0001) | 125,436 | Rules Regarding the Frequency and Notice of Continuing Disability Reviews |
| [FWS-R6-ES-2008-0008-0002](https://www.regulations.gov/document/FWS-R6-ES-2008-0008-0002) | 88,127 | Endangered and Threatened Wildlife and Plants; Designating the Northern Rocky Mountain Population of Gray Wolf as a Distinct Population Segment and Removing This Distinct Population Segment From the Federal List of Endangered and Threatened Wildlife |
| [WHD-2022-0003-0001](https://www.regulations.gov/document/WHD-2022-0003-0001) | 54,399 | Employee or Independent Contractor Classification under the Fair Labor Standards Act |
| [HHS-OPHS-2009-0001-0001](https://www.regulations.gov/document/HHS-OPHS-2009-0001-0001) | 53,207 | Rescission of the Regulation entitled "Ensuring That Department of Health and Human Services Funds Do Not Support Coercive or Discriminatory Policies or Practices in Violation of Federal Law" |
| [BSEE-2018-0002-0001](https://www.regulations.gov/document/BSEE-2018-0002-0001) | 46,813 | Oil and Gas and Sulfur Operations in Outer Continental Shelf: Blowout Preventer Systems and Well Control Revisions |
| [DEA-2023-0029-0001](https://www.regulations.gov/document/DEA-2023-0029-0001) | 35,458 | Telemedicine Prescribing of Controlled Substances When the Practitioner and the Patient Have Not Had a Prior In-Person Medical Evaluation |
| [FWS-R7-NWRS-2017-0058-0002](https://www.regulations.gov/document/FWS-R7-NWRS-2017-0058-0002) | 34,309 | Refuge-Specific Regulations; Public Use; Kenai National Wildlife Refuge |
| [CMS-2023-0016-0001](https://www.regulations.gov/document/CMS-2023-0016-0001) | 33,634 | Coverage of Certain Preventive Services under the Affordable Care Act |
| [CMS-2019-0006-0016](https://www.regulations.gov/document/CMS-2019-0006-0016) | 26,114 | Patient Protection and Affordable Care Act; HHS Notice of Benefit and Payment Parameters for 2020 |
| [VA-2019-VHA-0008-0001](https://www.regulations.gov/document/VA-2019-VHA-0008-0001) | 23,570 | AQ46-Proposed Rule-Veterans Community Care Program |
| [FMCSA-2004-19608-4095](https://www.regulations.gov/document/FMCSA-2004-19608-4095) | 23,526 | Hours of Service of Drivers, Proposed Rule, 75 FR 82170, December 29, 2010 |
| [FMCSA-1997-2350-0001](https://www.regulations.gov/document/FMCSA-1997-2350-0001) | 23,370 | Advanced Notice of Proposed Rulemaking - Hours of Service of Drivers |
| [FDA-2017-N-6565-0001](https://www.regulations.gov/document/FDA-2017-N-6565-0001) | 23,104 | Regulation of Flavors in Tobacco Products |
| [FAA-2004-17005-0001](https://www.regulations.gov/document/FAA-2004-17005-0001) | 21,549 | U.S. DOT/FAA - Notice of Proposed Rulemaking (NPRM) |
| [FTC-2023-0007-0001](https://www.regulations.gov/document/FTC-2023-0007-0001) | 21,125 | Non-Compete Clause Rule (NPRM) |
| [EPA-HQ-OW-2011-0880-0001](https://www.regulations.gov/document/EPA-HQ-OW-2011-0880-0001) | 20,594 | Clean Water Act; Definitions: Waters of the United States |
| [CMS-2010-0042-0001](https://www.regulations.gov/document/CMS-2010-0042-0001) | 18,745 | Revisions to Payment Policies Under the Physician Fee Schedule, and Other Part B Payment Policies; Revisions to Payment Policies for Ambulance Services for CY 2008; and the Proposed Elimination of the E-Rx Exemption for Computer-Generated Faxes*** |
| [NPS-2023-0001-0001](https://www.regulations.gov/document/NPS-2023-0001-0001) | 18,035 | Hunting and Trapping in National Preserves: Alaska |
| [ED-2019-OPE-0080-0001](https://www.regulations.gov/document/ED-2019-OPE-0080-0001) | 17,758 | Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards, Direct Grant Programs, State-Administered Formula Grant Programs, Developing Hispanic-Serving Institutions Program, and Strengthening Institutions Program |
| [FWS-HQ-NWRS-2022-0055-0001](https://www.regulations.gov/document/FWS-HQ-NWRS-2022-0055-0001) | 16,083 | 2022-2023 Station-Specific Hunting and Sport Fishing Regulations |
| [FWS-R4-ES-2018-0035-0001](https://www.regulations.gov/document/FWS-R4-ES-2018-0035-0001) | 14,780 | Endangered and Threatened Species: Nonessential Experimental Population of Red Wolves in Northeastern North Carolina |
| [FDA-2011-N-0921-0199](https://www.regulations.gov/document/FDA-2011-N-0921-0199) | 14,552 | Standards for the Growing, Harvesting, Packing, and Holding of Produce for Human Consumption; Extension of Comment Periods |
| [CMS-2014-0115-0002](https://www.regulations.gov/document/CMS-2014-0115-0002) | 13,764 | Coverage of Certain Preventive Services under the Affordable Care Act |
| [FDA-1978-N-0018-1648](https://www.regulations.gov/document/FDA-1978-N-0018-1648) | 13,716 | Sunscreen Drug Products for Over-the-Counter Human Use; Extension of Comment Period |
| [FWS-HQ-ES-2020-0047-48647](https://www.regulations.gov/document/FWS-HQ-ES-2020-0047-48647) | 12,923 | Endangered and Threatened Wildlife and Plants: Listing Endangered and Threatened Species and Designating Critical Habitat |

