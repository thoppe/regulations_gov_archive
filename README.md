# [Regulations.gov](https://www.regulations.gov/) archive

Data scrape and archive of regulations.gov using [v4 API](https://open.gsa.gov/api/regulationsgov/).

Regulations are organized by five document types: `Rule`, `Proposed Rule`, `Notice`, `Other`, and `Supporting & Related Material`. This project only collects documents on the first two types: `Rule` and `Proposed Rule`.

## Artifacts

+ [All documents and comment counts for `Rule` and `Proposed Rule`](artifacts/LISTING_rules_and_posted_rules.csv)


## Data Statistics
|     |     |
|---- |---- |
| Total documents | 133,096    |
| Unique agencies | 252    |
| Unique dockets  | 61,950   |
| Unique FR IDs   | 104,644      |
| Total comments  | 4,434,740  |

## Data ingestion progress
|     |     |
|---- |---- |
| Latest date   | 2023-08-16 |
| Earliest date | 1971-01-01    |
| Fraction of documents scanned for comments  | 0.2122 |

## Top 30 documents with most comments
| docId | comments | Title |
|------|---------:|-------|
| [CEQ-2019-0003-0001](https://www.regulations.gov/document/CEQ-2019-0003-0001) | 720,597 | Update to the Regulations Implementing the Procedural Provisions of the National Environmental Policy Act |
| [ED-2021-OCR-0166-0001](https://www.regulations.gov/document/ED-2021-OCR-0166-0001) | 238,987 | Nondiscrimination on the Basis of Sex in Education Programs or Activities Receiving Federal Financial Assistance |
| [CFPB-2016-0025-0001](https://www.regulations.gov/document/CFPB-2016-0025-0001) | 211,885 | Payday, Vehicle Title, and Certain High-Cost Installment Loans |
| [HHS-OS-2018-0008-0001](https://www.regulations.gov/document/HHS-OS-2018-0008-0001) | 204,771 | Compliance with Statutory Program Integrity Requirements |
| [FDA-2021-N-1349-0001](https://www.regulations.gov/document/FDA-2021-N-1349-0001) | 175,299 | Tobacco Product Standard for Menthol in Cigarettes |
| [ED-2022-OCR-0143-0001](https://www.regulations.gov/document/ED-2022-OCR-0143-0001) | 156,158 | Nondiscrimination on the Basis of Sex in Education Programs or Activities Receiving Federal Financial Assistance: Sex-Related Eligibility Criteria for Male and Female Athletic Teams |
| [SSA-2018-0026-0001](https://www.regulations.gov/document/SSA-2018-0026-0001) | 125,436 | Rules Regarding the Frequency and Notice of Continuing Disability Reviews |
| [FWS-HQ-ES-2018-0097-0001](https://www.regulations.gov/document/FWS-HQ-ES-2018-0097-0001) | 107,696 | Endangered and Threatened Wildlife and Plants; Removing the Gray Wolf (Canis lupus) from the List of Endangered and Threatened Wildlife |
| [ICEB-2018-0002-0001](https://www.regulations.gov/document/ICEB-2018-0002-0001) | 98,208 | Apprehension, Processing, Care, and Custody of Alien Minors and Unaccompanied Alien Children |
| [HHS-OS-2016-0014-0001](https://www.regulations.gov/document/HHS-OS-2016-0014-0001) | 92,458 | Compliance with Title X Requirements by Project Recipients in Selecting Subrecipients |
| [FWS-R6-ES-2008-0008-0002](https://www.regulations.gov/document/FWS-R6-ES-2008-0008-0002) | 88,127 | Endangered and Threatened Wildlife and Plants; Designating the Northern Rocky Mountain Population of Gray Wolf as a Distinct Population Segment and Removing This Distinct Population Segment From the Federal List of Endangered and Threatened Wildlife |
| [HHS-OS-2011-0023-0002](https://www.regulations.gov/document/HHS-OS-2011-0023-0002) | 84,088 | Group Health Plans and Health Insurance Issuers Relating to Coverage of Preventive Services under Patient Protection and Affordable Care Act: Amendment |
| [FNS-2022-0043-0001](https://www.regulations.gov/document/FNS-2022-0043-0001) | 74,006 | Child Nutrition Programs: Revisions to Meal Patterns Consistent with the 2020 Dietary Guidelines for Americans |
| [FDA-2021-N-1309-0001](https://www.regulations.gov/document/FDA-2021-N-1309-0001) | 71,523 | Tobacco Product Standard for Characterizing Flavors in Cigars |
| [USCIS-2010-0012-0001](https://www.regulations.gov/document/USCIS-2010-0012-0001) | 63,689 | Inadmissibility on Public Charge Grounds |
| [WHD-2019-0001-0001](https://www.regulations.gov/document/WHD-2019-0001-0001) | 59,348 | Defining and Delimiting the Exemptions for Executive, Administrative, Professional, Outside Sales and Computer Employees |
| [CFPB-2023-0010-0001](https://www.regulations.gov/document/CFPB-2023-0010-0001) | 56,084 | Credit Card Penalty Fees (Regulation Z) |
| [WHD-2022-0003-0001](https://www.regulations.gov/document/WHD-2022-0003-0001) | 54,399 | Employee or Independent Contractor Classification under the Fair Labor Standards Act |
| [HHS-OPHS-2009-0001-0001](https://www.regulations.gov/document/HHS-OPHS-2009-0001-0001) | 53,207 | Rescission of the Regulation entitled "Ensuring That Department of Health and Human Services Funds Do Not Support Coercive or Discriminatory Policies or Practices in Violation of Federal Law" |
| [FAA-2019-1100-0001](https://www.regulations.gov/document/FAA-2019-1100-0001) | 53,049 | Remote Identification of Unmanned Aircraft Systems |
| [APHIS-2017-0062-0001](https://www.regulations.gov/document/APHIS-2017-0062-0001) | 47,063 | Animal Welfare: Procedures for Applying for Licenses and Renewals |
| [BSEE-2018-0002-0001](https://www.regulations.gov/document/BSEE-2018-0002-0001) | 46,813 | Oil and Gas and Sulfur Operations in Outer Continental Shelf: Blowout Preventer Systems and Well Control Revisions |
| [DEA-2023-0029-0001](https://www.regulations.gov/document/DEA-2023-0029-0001) | 35,458 | Telemedicine Prescribing of Controlled Substances When the Practitioner and the Patient Have Not Had a Prior In-Person Medical Evaluation |
| [CMS-2021-0119-0053](https://www.regulations.gov/document/CMS-2021-0119-0053) | 35,318 | Medicare Program: CY 2022 Payment Policies Under the Physician Fee Schedule and Other Changes to Part B Payment Policies; Medicare Shared Savings Program Requirements; Provider Enrollment Regulation Updates; Provider and Supplier Prepayment and Post-Payment Medical Review Requirements (CMS-1751-P) |
| [ED-2021-OESE-0033-0001](https://www.regulations.gov/document/ED-2021-OESE-0033-0001) | 35,296 | Proposed Priorities: American History and Civics Education |
| [FWS-R7-NWRS-2017-0058-0002](https://www.regulations.gov/document/FWS-R7-NWRS-2017-0058-0002) | 34,309 | Refuge-Specific Regulations; Public Use; Kenai National Wildlife Refuge |
| [CMS-2023-0016-0001](https://www.regulations.gov/document/CMS-2023-0016-0001) | 33,634 | Coverage of Certain Preventive Services under the Affordable Care Act |
| [ED-2018-OPE-0027-0001](https://www.regulations.gov/document/ED-2018-OPE-0027-0001) | 31,918 | Student Assistance General Provisions, Federal Perkins Loan Program, Federal Family Education Loan Program, and William D. Ford Federal Direct Loan Program |
| [NLRB-2018-0001-0001](https://www.regulations.gov/document/NLRB-2018-0001-0001) | 28,986 | Definition of Joint Employer |
| [CMS-2019-0006-0016](https://www.regulations.gov/document/CMS-2019-0006-0016) | 26,114 | Patient Protection and Affordable Care Act; HHS Notice of Benefit and Payment Parameters for 2020 |

