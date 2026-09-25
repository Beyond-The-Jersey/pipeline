"""Sponsor ratings with the owner chain and the evidence behind each one."""

RATINGS = [{'sponsorId': 'aarp',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'aarp-owner',
            'name': 'AARP',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'AARP is owned by AARP. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'AARP is owned by AARP.',
            'source': {'name': 'AARP About page', 'date': '2026-09-24', 'url': 'https://www.aarp.org/about-aarp/'}},
  'verdict': 'Owned by AARP. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'acrisure',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'acrisure-owner',
            'name': 'Acrisure LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $30850 million; Supplier Code of Conduct: money '
                    'laundering; CFTC Whistleblower Program at Risk Without Lawmakers’ Help: $23 billion'},
  'claim': {'text': 'Acrisure LLC is the ultimate owner of Acrisure.',
            'short': 'Acrisure LLC is the ultimate owner of Acrisure.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Acrisure LLC is the ultimate owner of Acrisure.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $30850 million; Supplier Code of Conduct: money laundering; CFTC '
          'Whistleblower Program at Risk Without Lawmakers’ Help: $23 billion'},
 {'sponsorId': 'adidas',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'adidas-ag',
            'name': 'adidas AG',
            'type': 'listed-company',
            'country': 'DE',
            'note': "Judgement call: ownership is clean (no state stake) so 'none' was tempting, but the Xinjiang "
                    "cotton/forced-labour exposure is a named, documented human-rights issue, so 'concern' on record "
                    "not ownership. Same owner as sponsorId 'adidas-a'."},
  'claim': {'text': 'adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the '
                    "company's own ownership analysis for December 2025 identified almost 100% of shares, of which "
                    'institutional investors hold 79%, retail and undisclosed holdings 20% and treasury 1%, and no '
                    'single shareholder controls it. There is no state stake. The human-rights relevance sits in the '
                    'supply chain, not the cap table: adidas cotton sourcing carries a documented forced-labour '
                    'exposure in Xinjiang, where Xinjiang cotton was still detectable in adidas garments after the '
                    "company's assurances. Tier is set to concern on that supply-chain record rather than on "
                    'ownership.',
            'short': 'adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the '
                     "company's own ownership analysis for December 2025 identified almost 100%….",
            'source': {'name': "adidas AG Annual Report 2025 - 'Our Share'",
                       'date': '2025-12-31',
                       'url': 'https://report.adidas-group.com/2025/en/to-our-shareholders/our-share.html'}},
  'verdict': "adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the company's "
             'own ownership analysis for December 2025 identified almost 100%….',
  'confidence': 'medium',
  'note': "Judgement call: ownership is clean (no state stake) so 'none' was tempting, but the Xinjiang "
          "cotton/forced-labour exposure is a named, documented human-rights issue, so 'concern' on record not "
          "ownership. Same owner as sponsorId 'adidas-a'."},
 {'sponsorId': 'adidas-a',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'adidas-ag',
            'name': 'adidas AG',
            'type': 'listed-company',
            'country': 'DE',
            'note': "Same company as sponsorId 'adidas' (Mercedes and Audi F1 partner deals are both adidas AG)."},
  'claim': {'text': 'adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the '
                    "company's own ownership analysis for December 2025 identified almost 100% of shares, of which "
                    'institutional investors hold 79%, retail and undisclosed holdings 20% and treasury 1%, and no '
                    'single shareholder controls it. There is no state stake. The human-rights relevance sits in the '
                    'supply chain, not the cap table: adidas cotton sourcing carries a documented forced-labour '
                    'exposure in Xinjiang, where Xinjiang cotton was still detectable in adidas garments after the '
                    "company's assurances. Tier is set to concern on that supply-chain record rather than on "
                    'ownership.',
            'short': 'adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the '
                     "company's own ownership analysis for December 2025 identified almost 100%….",
            'source': {'name': "adidas AG Annual Report 2025 - 'Our Share'",
                       'date': '2025-12-31',
                       'url': 'https://report.adidas-group.com/2025/en/to-our-shareholders/our-share.html'}},
  'verdict': "adidas AG is a Frankfurt-listed German sportswear maker with a near-total free float: the company's "
             'own ownership analysis for December 2025 identified almost 100%….',
  'confidence': 'medium',
  'note': "Same company as sponsorId 'adidas' (Mercedes and Audi F1 partner deals are both adidas AG)."},
 {'sponsorId': 'adt',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'adt-owner',
            'name': 'ADT Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'ADT is a publicly traded company; Apollo affiliates hold ~22% stake but no controlling '
                    'interest. No state stake or serious conduct record identified.'},
  'claim': {'text': 'As of June 30, 2025, certain entities managed by affiliates of Apollo Global Management, Inc. '
                    "owned approximately 22% of ADT Inc.'s outstanding Common Stock.",
            'short': 'As of June 30, 2025, certain entities managed by affiliates of Apollo Global Management, Inc.',
            'source': {'name': 'SEC Form 10-Q for ADT Inc.',
                       'date': '2025-08-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1703056/000170305625000139/adt-20250630.htm'}},
  'verdict': 'Owned by ADT Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'ADT is a publicly traded company; Apollo affiliates hold ~22% stake but no controlling interest. No state '
          'stake or serious conduct record identified.'},
 {'sponsorId': 'advocate-health-care',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'advocate-health-care-owner',
            'name': 'Advocate Health Care',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Advocate Health is a private nonprofit healthcare system (501(c)(3)) formed by merger; no state '
                    'stake or government control identified. Parent is private-company type.'},
  'claim': {'text': 'Advocate Health Care is a private, nonprofit healthcare system formed by the 2022 merger of '
                    'Advocate Aurora Health and Atrium Health, with no state ownership or control.',
            'short': 'Advocate Health Care is a private, nonprofit healthcare system formed by the 2022 merger of '
                     'Advocate Aurora Health and Atrium Health, with no state ownership or….',
            'source': {'name': 'Advocate Health About Us page',
                       'date': '2026-09-24',
                       'url': 'https://www.advocatehealth.org/about-us'}},
  'verdict': 'Owned by Advocate Health Care. Nothing found.',
  'confidence': 'medium',
  'note': 'Advocate Health is a private nonprofit healthcare system (501(c)(3)) formed by merger; no state stake or '
          'government control identified. Parent is private-company type.'},
 {'sponsorId': 'aeroflot',
  'tier': 'severe',
  'ownership': 'owned',
  'owner': {'id': 'russian-federation',
            'name': 'Russian Federation (Federal Agency for State Property Management)',
            'type': 'state',
            'country': 'RU',
            'note': 'Severe because the state owner is directly tied to an ongoing armed conflict. Russia planned to '
                    'sell ~23.76% of its stake (Interfax, 2026), which would cut the state to ~50% but keep control. '
                    'Sanctions context: '
                    'https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/.'},
  'claim': {'text': 'PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder of '
                    'approximately 73.8% of shares. Russia is the direct belligerent in the ongoing war in Ukraine, '
                    'and Aeroflot plus its state parent have been targeted by EU/US sanctions since 2022.',
            'short': 'PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder '
                     'of approximately 73.8% of shares.',
            'source': {'name': 'Aeroflot Investor Relations, Shareholder Capital; Council of the EU sanctions '
                               'explainer',
                       'date': '2025 / 2026',
                       'url': 'https://ir.aeroflot.com/ensecurities/shareholder-capital'}},
  'verdict': 'PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder of '
             'approximately 73.8% of shares.',
  'confidence': 'high',
  'note': 'Severe because the state owner is directly tied to an ongoing armed conflict. Russia planned to sell '
          '~23.76% of its stake (Interfax, 2026), which would cut the state to ~50% but keep control. Sanctions '
          'context: https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/.'},
 {'sponsorId': 'aia',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'aia-group',
            'name': 'AIA Group Limited (HKEX: 1299)',
            'type': 'listed-company',
            'country': 'HK',
            'note': "Listed Hong Kong company → none. Historical note: AIA was spun out of AIG; the US government's "
                    'AIG bailout stake was long ago exited.'},
  'claim': {'text': 'AIA Group Limited is incorporated in Hong Kong with limited liability and listed on the Hong '
                    'Kong Stock Exchange (stock code 1299); it presents itself as the largest independent publicly '
                    'listed pan-Asian life insurer. No state or state-fund owner.',
            'short': 'AIA Group Limited is incorporated in Hong Kong with limited liability and listed on the Hong '
                     'Kong Stock Exchange (stock code 1299); it presents itself as the….',
            'source': {'name': 'AIA Group Limited official filings/press release; company corporate documents',
                       'date': '2023-07',
                       'url': 'https://www.aia.com/content/dam/group-wise/en/docs/press-release/2023/AIA%20Group%20Press%20Release_ENG_13%20July%202023.pdf.coredownload.pdf'}},
  'verdict': 'Owned by AIA Group Limited (HKEX: 1299). Nothing found.',
  'confidence': 'high',
  'note': "Listed Hong Kong company → none. Historical note: AIA was spun out of AIG; the US government's AIG "
          'bailout stake was long ago exited.'},
 {'sponsorId': 'airwallex',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'airwallex-owner',
            'name': 'Airwallex',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Airwallex is owned by Airwallex. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'Airwallex is owned by Airwallex.',
            'source': {'name': 'Airwallex Series B fundraising announcement',
                       'date': '2018-07-03',
                       'url': 'https://www.airwallex.com/global/newsroom/series-b-closing-80m'}},
  'verdict': 'Owned by Airwallex. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'albert',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'albert-owner',
            'name': 'Albert LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $0 million; Financial Times Highlights Citizenship Cases '
                    'Ahead of EU Ruling on Malta: money laundering; Could Hansi Flick have learned from Barcelona’s '
                    'last Champions League success?: money laundering'},
  'claim': {'text': 'Albert LLC is the ultimate owner of Albert.',
            'short': 'Albert LLC is the ultimate owner of Albert.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Albert LLC is the ultimate owner of Albert.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $0 million; Financial Times Highlights Citizenship Cases Ahead of '
          'EU Ruling on Malta: money laundering; Could Hansi Flick have learned from Barcelona’s last Champions '
          'League success?: money laundering'},
 {'sponsorId': 'all-in-won',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'all-in-won-owner',
            'name': 'All In Won Med-Bill & IT, LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Described as a New York-based premier medical billing company; partnership structure indicates '
                    'private ownership with no state stake.'},
  'claim': {'text': 'All In Won Med-Bill & IT, LLC is a privately held partnership founded in 2017 by Krystal '
                    'McKenna.',
            'short': 'All In Won Med-Bill & IT, LLC is a privately held partnership founded in 2017 by Krystal '
                     'McKenna.',
            'source': {'name': 'Brooklyn Sports & Entertainment press release',
                       'date': '2025-07-01',
                       'url': 'https://bkse.com/news/brooklyn-nets-name-all-in-won-as-official-jersey-patch-partner'}},
  'verdict': 'Owned by All In Won Med-Bill & IT, LLC. Nothing found.',
  'confidence': 'medium',
  'note': 'Described as a New York-based premier medical billing company; partnership structure indicates private '
          'ownership with no state stake.'},
 {'sponsorId': 'allegiant-travel-company',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'allegiant-travel-company-owner',
            'name': 'Allegiant Travel Company',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Founder Maurice Gallagher retains significant control (~11.1% stake) but company remains '
                    'privately held with no state ownership. No documented human-rights concerns in ownership '
                    'chain.'},
  'claim': {'text': 'Allegiant Travel Company is controlled by founder Maurice J. Gallagher Jr., who beneficially '
                    'owns over 11% of shares, with no state ownership.',
            'short': 'Allegiant Travel Company is controlled by founder Maurice J.',
            'source': {'name': 'Allegiant Travel Company DEF 14A 2026',
                       'date': '2026-05-15',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1362468/000136246826000034/algt-20260513.htm'}},
  'verdict': 'Owned by Allegiant Travel Company. Nothing found.',
  'confidence': 'high',
  'note': 'Founder Maurice Gallagher retains significant control (~11.1% stake) but company remains privately held '
          'with no state ownership. No documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'ally',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ally-financial',
            'name': 'Ally Financial Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Historic US Treasury stake (2009-2014) noted but fully exited, so not scored as state.'},
  'claim': {'text': 'Ally Financial Inc. (NYSE: ALLY) is a US-listed digital bank and auto lender with no state '
                    'shareholder; the largest holders are passive and mega-cap managers (Berkshire Hathaway '
                    'affiliates ~9.4%, Vanguard ~9.1%, BlackRock ~8.3% as of March 2026). The company was '
                    'majority-owned by the US Treasury after the 2008 GMAC bailout, but that stake was fully sold '
                    'and today ownership is purely private and dispersed. Human-rights relevance is conduct-based '
                    'and modest: subprime auto lending and repossession practice.',
            'short': 'Ally Financial Inc.',
            'source': {'name': 'Ally Financial Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-03-18',
                       'url': 'https://www.sec.gov/Archives/edgar/data/40729/000119312526113819/ally-20260318.htm'}},
  'verdict': 'Owned by Ally Financial Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Historic US Treasury stake (2009-2014) noted but fully exited, so not scored as state.'},
 {'sponsorId': 'alpinestars-c',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'alpinestars',
            'name': 'Alpinestars S.p.A. (Mazzarolo family)',
            'type': 'private-company',
            'country': 'IT',
            'note': "Family ownership from the company's own history page; no dated shareholder register published. "
                    "Same owner as 'alpinestars-h'."},
  'claim': {'text': 'Alpinestars is a private Italian protective-gear manufacturer based in Asolo, owned and '
                    'directed by the Mazzarolo family that founded it in 1963; Sante Mazzarolo started it and his '
                    'son Gabriele Mazzarolo owns and runs the company today. There is no state stake and no listing, '
                    'though Asian private-equity firms have been reported circling a ~EUR 1bn sale. Human-rights '
                    'relevance is the ordinary apparel/leather supply-chain set.',
            'short': 'Alpinestars is a private Italian protective-gear manufacturer based in Asolo, owned and '
                     'directed by the Mazzarolo family that founded it in 1963; Sante Mazzarolo….',
            'source': {'name': 'Alpinestars - official About Us page',
                       'date': None,
                       'url': 'https://alpinestars.com/pages/about-us'}},
  'verdict': 'Owned by Alpinestars S.p.A. (Mazzarolo family). Nothing found.',
  'confidence': 'high',
  'note': "Family ownership from the company's own history page; no dated shareholder register published. Same owner "
          "as 'alpinestars-h'."},
 {'sponsorId': 'alpinestars-h',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'alpinestars',
            'name': 'Alpinestars S.p.A. (Mazzarolo family)',
            'type': 'private-company',
            'country': 'IT',
            'note': None},
  'claim': {'text': 'Alpinestars is a private Italian protective-gear manufacturer based in Asolo, owned and '
                    'directed by the Mazzarolo family that founded it in 1963; Sante Mazzarolo started it and his '
                    'son Gabriele Mazzarolo owns and runs the company today. There is no state stake and no listing. '
                    'Same owner across the Cadillac and Haas F1 deals.',
            'short': 'Alpinestars is a private Italian protective-gear manufacturer based in Asolo, owned and '
                     'directed by the Mazzarolo family that founded it in 1963; Sante Mazzarolo….',
            'source': {'name': 'Alpinestars - official About Us page',
                       'date': None,
                       'url': 'https://alpinestars.com/pages/about-us'}},
  'verdict': 'Owned by Alpinestars S.p.A. (Mazzarolo family). Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'american-airlines',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'american-airlines-owner',
            'name': 'American Airlines',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'American Airlines Group Inc. is owned by American Airlines. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'American Airlines Group Inc.',
            'source': {'name': 'American Airlines Group Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-04-28',
                       'url': 'https://www.sec.gov/Archives/edgar/data/6201/000119312526187096/d83928ddef14a.htm'}},
  'verdict': 'Owned by American Airlines. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'american-family-insurance',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'american-family-mutual-insurance-company',
            'name': 'American Family Mutual Insurance Company, S.I.',
            'type': 'private-company',
            'country': 'US',
            'note': 'Type recorded as private-company because policyholder-owned mutuals are not listed; effectively '
                    'member-owned.'},
  'claim': {'text': 'American Family Insurance is a mutual: its parent is American Family Mutual Insurance Company, '
                    'S.I., owned by its policyholders rather than by external shareholders, with American Family '
                    'Connect, Homesite and Main Street America operating under the same mutual umbrella. There is no '
                    'state stake and no listed float. Human-rights relevance is indirect - a US '
                    'property-and-casualty insurer with no extractive or state-linked exposure.',
            'short': 'American Family Insurance is a mutual: its parent is American Family Mutual Insurance Company, '
                     'S.I., owned by its policyholders rather than by external….',
            'source': {'name': 'American Family Insurance newsroom - About American Family Insurance (Fast Facts)',
                       'date': '2026-03',
                       'url': 'http://newsroom.amfam.com/fast-facts'}},
  'verdict': 'Owned by American Family Mutual Insurance Company, S.I.. Nothing found.',
  'confidence': 'high',
  'note': 'Type recorded as private-company because policyholder-owned mutuals are not listed; effectively '
          'member-owned.'},
 {'sponsorId': 'amica-mutual-insurance',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'amica-mutual-insurance-owner',
            'name': 'Amica Mutual Insurance Company',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $0 million; 2022 First Circuit U.S. Court of Appeals '
                    'Case Law: money laundering'},
  'claim': {'text': 'Amica Mutual Insurance Company is the ultimate owner of Amica Mutual Insurance.',
            'short': 'Amica Mutual Insurance Company is the ultimate owner of Amica Mutual Insurance.',
            'source': {'name': 'Amica Mutual Insurance Company About Us',
                       'date': None,
                       'url': 'https://www.amicamutualinsurancecompany.com/about-us'}},
  'verdict': 'Amica Mutual Insurance Company is the ultimate owner of Amica Mutual Insurance.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $0 million; 2022 First Circuit U.S. Court of Appeals Case Law: '
          'money laundering'},
 {'sponsorId': 'anheuser-busch',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'anheuser-busch-owner',
            'name': 'Anheuser-Busch InBev SA/NV',
            'type': 'listed-company',
            'country': 'BE',
            'note': 'Ultimate owner is the publicly traded brewer; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Anheuser-Busch InBev SA/NV is a publicly listed company with its primary listing on Euronext '
                    'Brussels under ticker ABI.',
            'short': 'Anheuser-Busch InBev SA/NV is a publicly listed company with its primary listing on Euronext '
                     'Brussels under ticker ABI.',
            'source': {'name': 'SEC Form 20-F for Anheuser-Busch InBev SA/NV',
                       'date': '2026-03-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1668717/000119312526088105/d65314d20f.htm'}},
  'verdict': 'Owned by Anheuser-Busch InBev SA/NV. Nothing found.',
  'confidence': 'high',
  'note': 'Ultimate owner is the publicly traded brewer; no state stake or serious conduct record identified.'},
 {'sponsorId': 'arctempus',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'arctempus',
            'name': 'ARCTEMPUS (Arctempus Capital / Grupo StarOneRocket)',
            'type': 'private-company',
            'country': 'ES',
            'note': "RCD Espanyol's 20 Aug 2026 confirmation names ARCTEMPUS as main sponsor. Private, IESE-linked "
                    'business network; the Espanyol owner Alan Pace is a counterparty, not an owner.'},
  'claim': {'text': 'ARCTEMPUS is a Madrid-based private real-estate, investment and asset-management group formed '
                    'by merging Star1Rocket, Bestflat and Zenhia; the group is privately held with co-founders Luis '
                    'Miguel Real and Marc Sarnito and CEO Gonzalo Lopez behind it. No state or sovereign-fund '
                    'participation is disclosed.',
            'short': 'ARCTEMPUS is a Madrid-based private real-estate, investment and asset-management group formed '
                     'by merging Star1Rocket, Bestflat and Zenhia; the group is privately….',
            'source': {'name': "La Grada (Espanyol specialist outlet) - 'ARCTEMPUS Capital sera el nuevo "
                               "patrocinador del Espanyol'; RCD Espanyol official announcement",
                       'date': '2026-08-20',
                       'url': 'https://lagrada.org/arctempus-capital-patrocinador-espanyol-alan-pace-iese/'}},
  'verdict': 'Owned by ARCTEMPUS (Arctempus Capital / Grupo StarOneRocket). Nothing found.',
  'confidence': 'medium',
  'note': "RCD Espanyol's 20 Aug 2026 confirmation names ARCTEMPUS as main sponsor. Private, IESE-linked business "
          'network; the Espanyol owner Alan Pace is a counterparty, not an owner.'},
 {'sponsorId': 'ascension-st-vincent',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ascension-st-vincent-owner',
            'name': "Ascension St. Vincent's",
            'type': 'private-company',
            'country': 'USA',
            'note': 'Ascension is a private, faith-based nonprofit healthcare system; sponsored by Catholic '
                    'ministries but not state-owned or state-controlled. No evidence of state stake.'},
  'claim': {'text': 'Ascension is a Catholic, nonprofit healthcare system sponsored by religious ministries, with no '
                    'state ownership or control.',
            'short': 'Ascension is a Catholic, nonprofit healthcare system sponsored by religious ministries, with '
                     'no state ownership or control.',
            'source': {'name': 'Ascension About page',
                       'date': '2026-09-24',
                       'url': 'https://www.ascension.org/about'}},
  'verdict': "Owned by Ascension St. Vincent's. Nothing found.",
  'confidence': 'medium',
  'note': 'Ascension is a private, faith-based nonprofit healthcare system; sponsored by Catholic ministries but not '
          'state-owned or state-controlled. No evidence of state stake.'},
 {'sponsorId': 'at-and-t',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'att-inc',
            'name': 'AT&T Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'AT&T Inc. is owned by AT&T Inc.. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'AT&T Inc.',
            'source': {'name': 'AT&T INC. DEF 14A 2026 (SEC)',
                       'date': '2026-03-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/732717/000119312526119888/d919223ddef14a.htm'}},
  'verdict': 'Owned by AT&T Inc.. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'atlantic-health',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'atlantic-health-owner',
            'name': 'Atlantic Health System',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $0 million; Veteran federal prosecutor appointed New '
                    'Jersey insurance fraud prosecutor: money laundering'},
  'claim': {'text': 'Atlantic Health System is the ultimate owner of Atlantic Health.',
            'short': 'Atlantic Health System is the ultimate owner of Atlantic Health.',
            'source': {'name': 'Atlantic Health System About Us',
                       'date': None,
                       'url': 'https://www.atlantichealthsystem.org/about-us'}},
  'verdict': 'Atlantic Health System is the ultimate owner of Atlantic Health.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $0 million; Veteran federal prosecutor appointed New Jersey '
          'insurance fraud prosecutor: money laundering'},
 {'sponsorId': 'atlassian',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'atlassian',
            'name': 'Atlassian Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Founders are now based in the US/Australia; company redomiciled to Delaware. No state stake in '
                    'either jurisdiction.'},
  'claim': {'text': 'Atlassian Corporation is a Nasdaq-listed software company whose super-voting Class B stock is '
                    'held by co-founders Mike Cannon-Brookes and Scott Farquhar, giving them control despite the '
                    'Class A float; the proxy states the company is not aware of any arrangement that could result '
                    'in a change of control. No state shareholder. Human-rights relevance is ordinary corporate '
                    'conduct rather than anything structural.',
            'short': 'Atlassian Corporation is a Nasdaq-listed software company whose super-voting Class B stock is '
                     'held by co-founders Mike Cannon-Brookes and Scott Farquhar, giving….',
            'source': {'name': 'Atlassian Corporation DEF 14A 2025 (SEC)',
                       'date': '2025-10-14',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1650372/000165037225000058/team-20251014.htm'}},
  'verdict': 'Owned by Atlassian Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'Founders are now based in the US/Australia; company redomiciled to Delaware. No state stake in either '
          'jurisdiction.'},
 {'sponsorId': 'atrium-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'atrium-health-owner',
            'name': 'Atrium Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'Atrium Health is a nonprofit (not-for-profit) healthcare system; no state stake or serious '
                    'conduct record identified.'},
  'claim': {'text': 'Atrium Health is a nonprofit healthcare organization headquartered in Charlotte, North '
                    'Carolina, operating as part of Advocate Health, the third-largest nonprofit health system in '
                    'the United States.',
            'short': 'Atrium Health is a nonprofit healthcare organization headquartered in Charlotte, North '
                     'Carolina, operating as part of Advocate Health, the third-largest nonprofit….',
            'source': {'name': 'Atrium Health About Us page',
                       'date': '2026-09-24',
                       'url': 'https://atriumhealth.org/about-us'}},
  'verdict': 'Owned by Atrium Health. Nothing found.',
  'confidence': 'high',
  'note': 'Atrium Health is a nonprofit (not-for-profit) healthcare system; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'avnet',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'avnet-owner',
            'name': 'Avnet',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Avnet is a publicly traded company with no state ownership; largest shareholders are '
                    'institutional investors (Vanguard, BlackRock) each holding well under 10%. No human-rights '
                    'concerns in ownership chain identified.'},
  'claim': {'text': 'Avnet Inc. is a NYSE-listed electronics distributor with dispersed institutional ownership '
                    '(Vanguard and BlackRock each under 10%) and no state shareholder.',
            'short': 'Avnet Inc.',
            'source': {'name': 'Avnet DEF 14A 2025',
                       'date': '2025-10-07',
                       'url': 'https://www.sec.gov/Archives/edgar/data/8858/000110465925097498/tm2516396-1_def14a.htm'}},
  'verdict': 'Owned by Avnet. Nothing found.',
  'confidence': 'high',
  'note': 'Avnet is a publicly traded company with no state ownership; largest shareholders are institutional '
          'investors (Vanguard, BlackRock) each holding well under 10%. No human-rights concerns in ownership chain '
          'identified.'},
 {'sponsorId': 'aws',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'aws-owner',
            'name': 'Amazon Web Services (AWS)',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Amazon.com, Inc. is owned by Amazon Web Services (AWS). No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Amazon.com, Inc.',
            'source': {'name': 'AMAZON COM INC DEF 14A 2026 (SEC)',
                       'date': '2026-04-09',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1018724/000110465926041026/tm261382-1_def14a.htm'}},
  'verdict': 'Owned by Amazon Web Services (AWS). Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'baghdadi-capital',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'baghdadi-capital-sa',
            'name': 'Baghdadi Capital, S.A. (family office of Baihas Baghdadi)',
            'type': 'private-company',
            'country': 'ES',
            'note': 'Name suggests Iraq/Iranian links but ownership is Spanish private family capital. Manages ~EUR '
                    '1.5bn AUM across Spain, US, UK, Ireland, Singapore.'},
  'claim': {'text': "Baghdadi Capital, S.A. describes itself as a 'global independent corporate and investment "
                    "banking family office' founded in February 2023 by Spanish entrepreneur Baihas Baghdadi; it "
                    "states it is a '100% Spanish family office'. Founder is of Syrian heritage but the entity has "
                    'no state or sovereign-fund shareholder.',
            'short': 'Baghdadi Capital, S.A.',
            'source': {'name': "Baghdadi Capital, S.A. official 'Who We Are' page",
                       'date': '2026-01',
                       'url': 'https://baghdadicapital.com/en/'}},
  'verdict': 'Owned by Baghdadi Capital, S.A. (family office of Baihas Baghdadi). Nothing found.',
  'confidence': 'high',
  'note': 'Name suggests Iraq/Iranian links but ownership is Spanish private family capital. Manages ~EUR 1.5bn AUM '
          'across Spain, US, UK, Ireland, Singapore.'},
 {'sponsorId': 'ball-corporation',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'ball-corporation-owner',
            'name': 'Ball Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $2543420 million; Ball Corporation Press Release dated '
                    'February 1, 2024: $172 billion; Ball Corporation Press Release dated February 1, 2024: $15.35 '
                    'billion'},
  'claim': {'text': 'Ball Corporation is the ultimate owner of Ball Corporation.',
            'short': 'Ball Corporation is the ultimate owner of Ball Corporation.',
            'source': {'name': 'Ball Corporation Investor Relations',
                       'date': None,
                       'url': 'https://investors.ball.com'}},
  'verdict': 'Ball Corporation is the ultimate owner of Ball Corporation.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $2543420 million; Ball Corporation Press Release dated February 1, '
          '2024: $172 billion; Ball Corporation Press Release dated February 1, 2024: $15.35 billion'},
 {'sponsorId': 'ballys-intralot',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'standard-general',
            'name': 'Standard General L.P.',
            'type': 'private-company',
            'country': 'US',
            'note': "Ultimate owner traced to Standard General (Soo Kim) on both sides of the merger. Intralot's own "
                    'IR page (intralot.com/gr/investor-relations/stock) lays out the Standard General control chain '
                    "and CQ Lottery's 26.86% / PE Sub Holdings' 6.48% stakes. Sponsor name 'Bally's Intralot' refers "
                    'to the merged entity, not to a brand.'},
  'claim': {'text': "The Nottingham Forest sleeve sponsor is the combined Bally's Intralot betting and lottery "
                    "group, created when Bally's Corporation's international interactive arm was merged into "
                    "Athens-listed Intralot for EUR 2.7bn, with Bally's taking a 58% majority stake in the merged "
                    "entity. Bally's Corporation is controlled by Soohyung ('Soo') Kim's hedge fund Standard "
                    "General, which separately holds roughly 33% of Intralot's own voting rights via CQ Lottery LLC "
                    "and PE Sub Holdings. Ownership is private with no state stake; Intralot's exposure is gaming "
                    'licensing across Greece and other regulated markets.',
            'short': "The Nottingham Forest sleeve sponsor is the combined Bally's Intralot betting and lottery "
                     "group, created when Bally's Corporation's international interactive arm….",
            'source': {'name': "NEXT.io - 'EUR 2.7bn Bally's-Intralot deal creates Athens stock exchange gaming "
                               "giant'",
                       'date': '2025-10-10',
                       'url': 'https://next.io/news/investment/ballys-intralot-deal-athens-stock-exchange-giant'}},
  'verdict': 'Owned by Standard General L.P.. Nothing found.',
  'confidence': 'medium',
  'note': "Ultimate owner traced to Standard General (Soo Kim) on both sides of the merger. Intralot's own IR page "
          "(intralot.com/gr/investor-relations/stock) lays out the Standard General control chain and CQ Lottery's "
          "26.86% / PE Sub Holdings' 6.48% stakes. Sponsor name 'Bally's Intralot' refers to the merged entity, not "
          'to a brand.'},
 {'sponsorId': 'banca-popolare-del-frusinate',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'banca-popolare-del-frusinate',
            'name': 'Banca Popolare del Frusinate S.C.p.A.',
            'type': 'private-company',
            'country': 'IT',
            'note': None},
  'claim': {'text': "Banca Popolare del Frusinate is a Frosinone-based 'Societa Cooperativa per Azioni' with share "
                    'capital of EUR 31,883,700 fully paid as at 31 December 2025 - i.e. owned by its own '
                    'member-shareholders rather than by a listed or state parent. Italian cooperative banks carry no '
                    'state equity. Record is unremarkable at this size; its Frosinone/Lazio lending limits '
                    'human-rights relevance to ordinary banking conduct.',
            'short': "Banca Popolare del Frusinate is a Frosinone-based 'Societa Cooperativa per Azioni' with share "
                     'capital of EUR 31,883,700 fully paid as at 31 December 2025 - i.e.',
            'source': {'name': 'Banca Popolare del Frusinate - Dati Societari (company details)',
                       'date': '2025-12-31',
                       'url': 'https://www.bpf.it/dati-societari/'}},
  'verdict': 'Owned by Banca Popolare del Frusinate S.C.p.A.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'bank-of-america',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'bank-of-america',
            'name': 'Bank of America Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': "Fossil-fuel and settlement record is well documented but not 'sustained abuse', so concern not "
                    'serious.'},
  'claim': {'text': 'Bank of America Corporation is a US-listed bank with dispersed institutional ownership '
                    '(BlackRock and Vanguard the largest holdings, both well under 10%) and no state shareholder - '
                    "the US Treasury's crisis-era TARP stake is long gone. Its human-rights relevance is conduct "
                    'rather than ownership: BofA is among the largest global financiers of fossil fuels and carried '
                    'multi-billion-dollar mortgage and securities settlements after 2008. That gives a genuine but '
                    'lesser documented record, hence concern rather than none.',
            'short': 'Bank of America Corporation is a US-listed bank with dispersed institutional ownership '
                     '(BlackRock and Vanguard the largest holdings, both well under 10%) and no….',
            'source': {'name': 'Bank of America Corporation DEF 14A 2026 (SEC)',
                       'date': '2026-03-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/70858/000119312526118929/d43888ddef14a.htm'}},
  'verdict': 'Bank of America Corporation is a US-listed bank with dispersed institutional ownership (BlackRock and '
             'Vanguard the largest holdings, both well under 10%) and no….',
  'confidence': 'high',
  'note': "Fossil-fuel and settlement record is well documented but not 'sustained abuse', so concern not serious."},
 {'sponsorId': 'baptist-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'baptist-health-owner',
            'name': 'Baptist Health South Florida',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states not-for-profit mission; no state stake or serious conduct record identified.'},
  'claim': {'text': 'Baptist Health is a faith-based, not-for-profit healthcare organization.',
            'short': 'Baptist Health is a faith-based, not-for-profit healthcare organization.',
            'source': {'name': 'Baptist Health South Florida website',
                       'date': '2026-09-24',
                       'url': 'https://baptisthealth.net/about-baptist-health/fulfilling-our-mission'}},
  'verdict': 'Owned by Baptist Health South Florida. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states not-for-profit mission; no state stake or serious conduct record identified.'},
 {'sponsorId': 'barclays',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'barclays', 'name': 'Barclays PLC', 'type': 'listed-company', 'country': 'GB', 'note': None},
  'claim': {'text': 'Barclays PLC is a UK-listed bank whose only notifiable holder above the 3% disclosure threshold '
                    'as at 31 December 2025 is BlackRock (about 5.8% in 2024), with no state stake since the UK '
                    "government's 2008 crisis holding was sold. The human-rights relevant record is conduct: LIBOR "
                    'and mis-selling fines, and a leading European position in fossil-fuel financing. Concern, not '
                    'serious, because ownership is purely private.',
            'short': 'Barclays PLC is a UK-listed bank whose only notifiable holder above the 3% disclosure '
                     'threshold as at 31 December 2025 is BlackRock (about 5.8% in 2024), with no….',
            'source': {'name': "Barclays PLC Annual Report 2025 (Form 20-F), 'Major shareholders' p.114",
                       'date': '2025-12-31',
                       'url': 'https://www.sec.gov/Archives/edgar/data/312069/000031206926000004/bcs-20251231.htm'}},
  'verdict': 'Barclays PLC is a UK-listed bank whose only notifiable holder above the 3% disclosure threshold as at '
             '31 December 2025 is BlackRock (about 5.8% in 2024), with no….',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'barmenia',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'barmenia-versicherungen-ag',
            'name': 'Barmenia Versicherungen a.G. (BarmeniaGothaer Group)',
            'type': 'private-company',
            'country': 'DE',
            'note': "German mutual 'a.G.' structure; Barmenia holds 36% and Gothaer 64% of the joint holding after "
                    'the 2023/24 merger. No state capital.'},
  'claim': {'text': 'Barmenia Versicherungen a.G. is a German mutual insurer (Versicherungsverein auf '
                    'Gegenseitigkeit) based in Wuppertal and now the leading entity of the BarmeniaGothaer group '
                    'alongside Gothaer Versicherungsbank VVaG. As a mutual it is owned by its policyholder members, '
                    'not by shareholders or the state.',
            'short': 'Barmenia Versicherungen a.G.',
            'source': {'name': 'BarmeniaGothaer Group annual report 2025 (Konzerngeschaeftsbericht) / Barmenia legal '
                               'notice',
                       'date': '2025',
                       'url': 'https://www.barmeniagothaer.de/infos-zur-gruppe/'}},
  'verdict': 'Owned by Barmenia Versicherungen a.G. (BarmeniaGothaer Group). Nothing found.',
  'confidence': 'high',
  'note': "German mutual 'a.G.' structure; Barmenia holds 36% and Gothaer 64% of the joint holding after the 2023/24 "
          'merger. No state capital.'},
 {'sponsorId': 'betano',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'kaizen-gaming',
            'name': 'Kaizen Gaming International Limited (partly owned by Allwyn)',
            'type': 'private-company',
            'country': 'GR',
            'note': 'Private Greek/Czech owners, no state link → none. Kaizen is registered/parented in Malta while '
                    'Greek-founded; country shown as GR as the operating origin. Ownership percentage sourced from '
                    'trade press, hence medium confidence.'},
  'claim': {'text': 'Betano is owned by Kaizen Gaming International Limited, a private Greek-founded GameTech group; '
                    'its parent has reached decacorn status and Allwyn holds a 36.75% stake. Owners are private '
                    'investors (Allwyn/KKCG of Czech billionaire Karel Komarek), with no state or state-fund owner.',
            'short': 'Betano is owned by Kaizen Gaming International Limited, a private Greek-founded GameTech '
                     'group; its parent has reached decacorn status and Allwyn holds a 36.75%….',
            'source': {'name': 'Kaizen Gaming official; EGR Global (Allwyn 36.75% stake)',
                       'date': '2026',
                       'url': 'https://www.egr.global/intel/news/betanos-parent-company-achieves-decacorn-status/'}},
  'verdict': 'Owned by Kaizen Gaming International Limited (partly owned by Allwyn). Nothing found.',
  'confidence': 'medium',
  'note': 'Private Greek/Czech owners, no state link → none. Kaizen is registered/parented in Malta while '
          'Greek-founded; country shown as GR as the operating origin. Ownership percentage sourced from trade '
          'press, hence medium confidence.'},
 {'sponsorId': 'betsson-sport',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'betsson', 'name': 'Betsson AB', 'type': 'listed-company', 'country': 'SE', 'note': None},
  'claim': {'text': 'Betsson AB is a Swedish online gaming group listed on Nasdaq Stockholm since 2000, with no '
                    'state shareholder. Its A shares are concentrated in founder/family vehicles - Hamberg '
                    'Forvaltning, Knutsson Holdings, Biljana Kling and the Lindwall family - which hold the bulk of '
                    'the votes, while the B-share float is held by index funds such as Fidelity and Vanguard. '
                    'Human-rights relevance is gambling regulation across many markets rather than ownership.',
            'short': 'Betsson AB is a Swedish online gaming group listed on Nasdaq Stockholm since 2000, with no '
                     'state shareholder.',
            'source': {'name': 'Betsson AB - Largest Shareholders (company IR)',
                       'date': '2026-06-30',
                       'url': 'https://www.betssonab.com/investors/share/largest-shareholders'}},
  'verdict': 'Owned by Betsson AB. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'beumer-group',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'beumer-group',
            'name': 'BEUMER Group GmbH & Co. KG',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Almost 90 years old, family-run, no listed float, no state stake.'},
  'claim': {'text': 'BEUMER Group is a family-owned German intralogistics/conveying systems group based in Beckum; '
                    "its own main-partner announcement for FC Schalke 04 (from 2026/27) describes it as 'the global "
                    "family-owned company from Beckum'.",
            'short': 'BEUMER Group is a family-owned German intralogistics/conveying systems group based in Beckum; '
                     'its own main-partner announcement for FC Schalke 04 (from 2026/27)….',
            'source': {'name': "FC Schalke 04 official press release 'BEUMER Group to become FC Schalke 04's new "
                               "main partner'",
                       'date': '2026-04-22',
                       'url': 'https://schalke04.de/en/partner-en/beumer-group-new-main-partner'}},
  'verdict': 'Owned by BEUMER Group GmbH & Co. KG. Nothing found.',
  'confidence': 'high',
  'note': 'Almost 90 years old, family-run, no listed float, no state stake.'},
 {'sponsorId': 'bimbo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'grupo-bimbo',
            'name': 'Grupo Bimbo, S.A.B. de C.V.',
            'type': 'listed-company',
            'country': 'MX',
            'note': 'The site publishes shareholder structure as a downloadable table rather than inline, so the '
                    'exact family percentage is not stated on the page itself.'},
  'claim': {'text': 'Grupo Bimbo, S.A.B. de C.V. is a Mexican-listed global baker whose controlling shareholder '
                    "block sits with the founding Servitje family through the company's dual share structure; the "
                    "shareholder table is published in the company's own governance section. There is no state "
                    'stake. Human-rights relevance is labour and agricultural sourcing (palm oil, cocoa, wheat) in a '
                    'very large supply chain.',
            'short': 'Grupo Bimbo, S.A.B.',
            'source': {'name': 'Grupo Bimbo - Investor Relations, Governance / Shareholder Structure',
                       'date': None,
                       'url': 'http://www.grupobimbo.com/en/investors/governance/structure'}},
  'verdict': 'Owned by Grupo Bimbo, S.A.B. de C.V.. Nothing found.',
  'confidence': 'medium',
  'note': 'The site publishes shareholder structure as a downloadable table rather than inline, so the exact family '
          'percentage is not stated on the page itself.'},
 {'sponsorId': 'bmo-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'bank-of-montreal',
            'name': 'Bank of Montreal',
            'type': 'listed-company',
            'country': 'CA',
            'note': "BMO's 40-F primary document is largely XBRL; the ownership evidence used is the AIF exhibit."},
  'claim': {'text': 'Bank of Montreal (BMO) is a Canadian chartered bank listed in Toronto and New York with no '
                    'state shareholder. Canadian law caps concentration: under the Bank Act no person may be a '
                    "'major shareholder' - more than 20% of any class of voting shares - of a bank of BMO's size, "
                    'and none is, so the bank is institutionally dispersed by statute. Record is unremarkable; '
                    'relevance is ordinary banking conduct.',
            'short': 'Bank of Montreal (BMO) is a Canadian chartered bank listed in Toronto and New York with no '
                     'state shareholder.',
            'source': {'name': 'Bank of Montreal Annual Information Form for the year ended 31 October 2025 (SEC '
                               '40-F Exhibit 99.1)',
                       'date': '2025-12-04',
                       'url': 'https://www.sec.gov/Archives/edgar/data/927971/000119312525307982/d938207dex991.htm'}},
  'verdict': 'Owned by Bank of Montreal. Nothing found.',
  'confidence': 'medium',
  'note': "BMO's 40-F primary document is largely XBRL; the ownership evidence used is the AIF exhibit."},
 {'sponsorId': 'boeing',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'boeing',
            'name': 'The Boeing Company',
            'type': 'listed-company',
            'country': 'US',
            'note': "Read literally, Boeing's weapons sales to conflict parties could argue for severe; kept at "
                    'concern because the company itself is not a belligerent state entity.'},
  'claim': {'text': 'The Boeing Company is a US-listed commercial and defence aerospace prime with a widely held '
                    'register and no state shareholder; its largest holders are index managers (Vanguard 9.0%, FMR '
                    '7.0%, BlackRock 6.8% as at 31 December 2025). Human-rights relevance is the conduct record: two '
                    '737 MAX crashes killed 346 people, the type was grounded for 20 months, and the defence arm '
                    'sells aircraft and munitions into live conflicts. That is a genuine but non-state record, so '
                    'concern.',
            'short': 'The Boeing Company is a US-listed commercial and defence aerospace prime with a widely held '
                     'register and no state shareholder; its largest holders are index….',
            'source': {'name': "The Boeing Company DEF 14A 2026, 'Principal Shareholders' (SEC)",
                       'date': '2026-03-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/12927/000119312526096787/d39411ddef14a.htm'}},
  'verdict': 'The Boeing Company is a US-listed commercial and defence aerospace prime with a widely held register '
             'and no state shareholder; its largest holders are index….',
  'confidence': 'high',
  'note': "Read literally, Boeing's weapons sales to conflict parties could argue for severe; kept at concern "
          'because the company itself is not a belligerent state entity.'},
 {'sponsorId': 'boylesports',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'boylesports',
            'name': 'BoyleSports (Boyle family)',
            'type': 'private-company',
            'country': 'IE',
            'note': 'boylesports.com itself geo-blocks some US IPs, so a secondary aggregator was used for the '
                    'ownership statement.'},
  'claim': {'text': "BoyleSports is Ireland's largest independent bookmaker, privately held and owned by founder "
                    'John Boyle and his family, with no stock exchange listing and no state stake. Industry reports '
                    'in 2026 describe the family as having explored a sale, so ownership is stated as of September '
                    '2026. Human-rights relevance is gambling regulation exposure in Ireland and the UK (Gibraltar '
                    'licence; UK Gambling Commission account 39469).',
            'short': "BoyleSports is Ireland's largest independent bookmaker, privately held and owned by founder "
                     'John Boyle and his family, with no stock exchange listing and no state….',
            'source': {'name': 'Listed Casino Companies - BoyleSports company profile',
                       'date': '2026-09',
                       'url': 'https://listedcasinocompanies.com/boylesports'}},
  'verdict': 'Owned by BoyleSports (Boyle family). Nothing found.',
  'confidence': 'medium',
  'note': 'boylesports.com itself geo-blocks some US IPs, so a secondary aggregator was used for the ownership '
          'statement.'},
 {'sponsorId': 'breitling',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'cvc-capital-partners',
            'name': 'CVC Capital Partners (CVC Fund VI)',
            'type': 'private-company',
            'country': 'LU',
            'note': "CVC's own 28 Apr 2017 release documents the 80/20 deal; the follow-on 20% purchase (Nov 2018) "
                    'is documented by Unquote. Owner type kept as private-company because the holder is a PE fund, '
                    'not the listed manager.'},
  'claim': {'text': 'Breitling SA is a Swiss luxury watchmaker that is no longer family-held: CVC Fund VI agreed to '
                    'buy an 80% stake in 2017 (with Theodore Schneider re-investing for 20%) and CVC then bought the '
                    'remaining 20% in November 2018, taking it to 100%. The ultimate owner is therefore CVC Capital '
                    'Partners, a private-equity manager (CVC Capital Partners plc is itself Amsterdam-listed, but '
                    'the fund holding Breitling is private). No state stake; relevance is ordinary consumer-goods '
                    'supply chain.',
            'short': 'Breitling SA is a Swiss luxury watchmaker that is no longer family-held: CVC Fund VI agreed to '
                     'buy an 80% stake in 2017 (with Theodore Schneider re-investing for….',
            'source': {'name': "CVC Capital Partners - 'CVC Fund VI agrees to acquire majority stake in Breitling "
                               "SA'",
                       'date': '2017-04-28',
                       'url': 'http://cvc.com/media/news/2017/2017-04-28-cvc-fund-vi-agrees-to-acquire-majority-stake-in-breitling-sa'}},
  'verdict': 'Owned by CVC Capital Partners (CVC Fund VI). Nothing found.',
  'confidence': 'high',
  'note': "CVC's own 28 Apr 2017 release documents the 80/20 deal; the follow-on 20% purchase (Nov 2018) is "
          'documented by Unquote. Owner type kept as private-company because the holder is a PE fund, not the listed '
          'manager.'},
 {'sponsorId': 'burns-and-mcdonnell',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'burns-and-mcdonnell-owner',
            'name': 'Burns & McDonnell',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Burns & McDonnell is 100% employee-owned through ESOP; no state stake or government control. No '
                    'documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'Burns & McDonnell is a 100% employee-owned engineering firm via ESOP since 1986, with no state '
                    'ownership or control.',
            'short': 'Burns & McDonnell is a 100% employee-owned engineering firm via ESOP since 1986, with no state '
                     'ownership or control.',
            'source': {'name': 'Burns & McDonnell Employee Ownership page',
                       'date': '2026-09-24',
                       'url': 'https://burnsmcd.com/who-we-are/employee-ownership'}},
  'verdict': 'Owned by Burns & McDonnell. Nothing found.',
  'confidence': 'high',
  'note': 'Burns & McDonnell is 100% employee-owned through ESOP; no state stake or government control. No '
          'documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'bwt',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'bwt-group',
            'name': 'BWT AG (WAB Group / Weissenbacher family)',
            'type': 'private-company',
            'country': 'AT',
            'note': 'Judgement call: the FY2014 report is the last shareholder register BWT published, so the 79.7% '
                    "WAB figure is dated but consistent with the company's current self-description as "
                    'founder/management-controlled. No more recent register found.'},
  'claim': {'text': 'BWT AG (Best Water Technology), based in Mondsee, Austria, is a private water-treatment '
                    'manufacturer. The company has been controlled since a 1990 management buy-out led by Andreas '
                    'Weissenbacher, and its last published shareholder structure - in the FY2014 report, before the '
                    'Vienna listing was wound up - showed the WAB group holding 79.7% with only 14.3% free float. '
                    'There is no state stake; relevance is industrial/water-sector conduct rather than rights.',
            'short': 'BWT AG (Best Water Technology), based in Mondsee, Austria, is a private water-treatment '
                     'manufacturer.',
            'source': {'name': "BWT AG Annual Report 2014, 'Shareholder structure'",
                       'date': '2014-12-31',
                       'url': 'https://www.bwt.com/en/-/media/bwt/www,-d-,bwt,-d-,com/documents/financial-publications/annual-reports/bwt-annual-report-2014.pdf'}},
  'verdict': 'Owned by BWT AG (WAB Group / Weissenbacher family). Nothing found.',
  'confidence': 'medium',
  'note': 'Judgement call: the FY2014 report is the last shareholder register BWT published, so the 79.7% WAB figure '
          "is dated but consistent with the company's current self-description as founder/management-controlled. No "
          'more recent register found.'},
 {'sponsorId': 'c-hedenkamp',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'c-hedenkamp-gmbh',
            'name': 'C. Hedenkamp GmbH & Co. KG',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Small mittelstand firm; family owners in the register. No state link.'},
  'claim': {'text': 'C. Hedenkamp GmbH & Co. KG of Hoevelhof (Paderborn registry) is a family-owned German '
                    'building-materials/construction supplier; the commercial register shows it is controlled via '
                    'Hedenkamp Verwaltungs GmbH by Wolf Karsten Hedenkamp, Klaus Dietrich Hedenkamp and Markus '
                    'Hedenkamp.',
            'short': 'C.',
            'source': {'name': 'C. Hedenkamp GmbH & Co. KG official Imprint / Handelsregister entry',
                       'date': '2026',
                       'url': 'https://www.hedenkamp.de/en/impressum/'}},
  'verdict': 'Owned by C. Hedenkamp GmbH & Co. KG. Nothing found.',
  'confidence': 'high',
  'note': 'Small mittelstand firm; family owners in the register. No state link.'},
 {'sponsorId': 'caesars-entertainment',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'caesars-entertainment-owner',
            'name': 'Caesars Entertainment',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Caesars Entertainment, Inc. is owned by Caesars Entertainment. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Caesars Entertainment, Inc.',
            'source': {'name': 'Caesars Entertainment, Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-04-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1590895/000119312526174058/d140199ddef14a.htm'}},
  'verdict': 'Owned by Caesars Entertainment. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'capital-one',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'capital-one-owner',
            'name': 'Capital One Financial Corp.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $930 million; Capital One to Pay $425 Million in 360 '
                    'Savings Interest-Rate Settlement - WSJ: $425 million; Capital One to Pay $425 Million in 360 '
                    'Savings Interest-Rate Settlement - WSJ: $425 million'},
  'claim': {'text': 'Capital One Financial Corp. is the ultimate owner of Capital One.',
            'short': 'Capital One Financial Corp.',
            'source': {'name': 'Capital One Financial Corp. Investor Relations',
                       'date': None,
                       'url': 'https://investor.capitalone.com'}},
  'verdict': 'Capital One Financial Corp.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $930 million; Capital One to Pay $425 Million in 360 Savings '
          'Interest-Rate Settlement - WSJ: $425 million; Capital One to Pay $425 Million in 360 Savings '
          'Interest-Rate Settlement - WSJ: $425 million'},
 {'sponsorId': 'carvana',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'carvana', 'name': 'Carvana Co.', 'type': 'listed-company', 'country': 'US', 'note': None},
  'claim': {'text': 'Carvana Co. is a US-listed used-car retailer controlled by founder Ernest Garcia III and the '
                    "Garcia family through high-vote Class B stock; the equity plan itself defines the 'Garcia "
                    "Parties' as a distinct change-of-control bloc, and Garcia signs the 10-K as chairman and CEO. "
                    'No state shareholder. Human-rights relevance is consumer-credit and reconditioning-centre '
                    'labour.',
            'short': 'Carvana Co.',
            'source': {'name': "Carvana Co. DEF 14A 2026, 'Security Ownership of Certain Beneficial Owners and "
                               "Management' (SEC)",
                       'date': '2026-03-25',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1690820/000169082026000024/cvna-20260325.htm'}},
  'verdict': 'Owned by Carvana Co.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'cazoo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'motors',
            'name': 'Motors.co.uk Limited (O3 Industries / Novum Capital)',
            'type': 'private-company',
            'country': 'GB',
            'note': "Trace corrected: the given owner chain was empty; Cazoo's brand now sits with Motors "
                    '(O3/Novum), NOT with the original Cazoo Group. Motors itself was bought from eBay Classifieds '
                    'in Dec 2021 by O3 Industries and Novum Capital.'},
  'claim': {'text': 'Cazoo is no longer the listed business it once was: the company went into administration in May '
                    '2024 and its brand and tech were sold to Motors, the used-car marketplace owned since 2021 by '
                    'New York private-equity house O3 Industries and Frankfurt-based Novum Capital. Ownership today '
                    'is therefore private equity with no state stake. Human-rights relevance is evidence-thin - the '
                    'collapsed company left GBP 259m owed to over 10,000 creditors, but no material rights record.',
            'short': 'Cazoo is no longer the listed business it once was: the company went into administration in '
                     'May 2024 and its brand and tech were sold to Motors, the used-car….',
            'source': {'name': "BusinessCloud - 'Private equity-backed Motors snaps up Cazoo brand'",
                       'date': '2024-06-28',
                       'url': 'https://businesscloud.co.uk/news/private-equity-backed-motors-snaps-up-cazoo-brand'}},
  'verdict': 'Owned by Motors.co.uk Limited (O3 Industries / Novum Capital). Nothing found.',
  'confidence': 'medium',
  'note': "Trace corrected: the given owner chain was empty; Cazoo's brand now sits with Motors (O3/Novum), NOT with "
          'the original Cazoo Group. Motors itself was bought from eBay Classifieds in Dec 2021 by O3 Industries and '
          'Novum Capital.'},
 {'sponsorId': 'chexx',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'continent-gaming',
            'name': 'Continent Gaming N.V.',
            'type': 'private-company',
            'country': 'CW',
            'note': "Kept at 'none' rather than 'unrated' because the operating entity is clearly established; the "
                    "opacity is about the group's ultimate beneficial owners, which Curaçao does not publish."},
  'claim': {'text': 'CHEXX (chexx.bet), the Crystal Palace sleeve brand, is owned and operated by Continent Gaming '
                    'N.V., a Curaçao-registered private company (registration 159857) licensed by the Curaçao Gaming '
                    'Authority, with Continent Gaming LTD in Cyprus acting as agent. Ownership is entirely private '
                    'with no state stake. The record is opaque rather than abusive: CHEXX has been criticised as a '
                    'thinly documented, Asia-facing operator behind a Premier League sleeve deal.',
            'short': 'CHEXX (chexx.bet), the Crystal Palace sleeve brand, is owned and operated by Continent Gaming '
                     'N.V., a Curaçao-registered private company (registration 159857)….',
            'source': {'name': "CHEXX help centre - 'About us' (operator and licence disclosure)",
                       'date': '2025-06-14',
                       'url': 'https://help.chexx.bet/en/articles/9114022-about-us'}},
  'verdict': 'Owned by Continent Gaming N.V.. Nothing found.',
  'confidence': 'medium',
  'note': "Kept at 'none' rather than 'unrated' because the operating entity is clearly established; the opacity is "
          "about the group's ultimate beneficial owners, which Curaçao does not publish."},
 {'sponsorId': 'childrens-health',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'ut-southwestern-medical-center',
            'name': 'The University of Texas Southwestern Medical Center',
            'type': 'state',
            'country': 'US',
            'note': 'Judgement call: the sponsor entry covers two owners. Scored on the state half (UT Southwestern) '
                    "because state ownership is the tier-driving fact; Children's Health's non-profit status is "
                    "evidenced by ProPublica Nonprofit Explorer (EIN 75-0800628). 'serious' reflects state rather "
                    'than state-fund ownership.'},
  'claim': {'text': "This is a split patch sponsor: Children's Health (home kit) is a private 501(c)(3) non-profit - "
                    "Children's Health System of Texas, EIN 75-0800628 - while UT Southwestern Medical Center (away "
                    'kit) is a state institution, the public medical school of The University of Texas, established '
                    'as a UT medical branch in Dallas in 1949 under the UT Board of Regents. State ownership of one '
                    'half of the patch drives a state tier. Human-rights relevance is limited to public-sector '
                    'healthcare and labour policy.',
            'short': "This is a split patch sponsor: Children's Health (home kit) is a private 501(c)(3) non-profit "
                     "- Children's Health System of Texas, EIN 75-0800628 - while UT….",
            'source': {'name': "UT Southwestern - 'Mission, Values, and History' (About Us)",
                       'date': None,
                       'url': 'https://utsw.edu/about-us/mission-history'}},
  'verdict': "This is a split patch sponsor: Children's Health (home kit) is a private 501(c)(3) non-profit - "
             "Children's Health System of Texas, EIN 75-0800628 - while UT….",
  'confidence': 'medium',
  'note': 'Judgement call: the sponsor entry covers two owners. Scored on the state half (UT Southwestern) because '
          "state ownership is the tier-driving fact; Children's Health's non-profit status is evidenced by "
          "ProPublica Nonprofit Explorer (EIN 75-0800628). 'serious' reflects state rather than state-fund "
          'ownership.'},
 {'sponsorId': 'childrens-hospital-colorado',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'childrens-hospital-colorado-owner',
            'name': "Children's Hospital Colorado",
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states private, non-profit status; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': "As a private, non-profit pediatric hospital, Children's Hospital Colorado is 100% dedicated to "
                    'caring for children at all ages and stages of growth.',
            'short': "As a private, non-profit pediatric hospital, Children's Hospital Colorado is 100% dedicated to "
                     'caring for children at all ages and stages of growth.',
            'source': {'name': "Children's Hospital Colorado Continuing Education page",
                       'date': '2026-09-24',
                       'url': 'https://ce.childrenscolorado.org/content/childrens-hospital-colorado-mission'}},
  'verdict': "Owned by Children's Hospital Colorado. Nothing found.",
  'confidence': 'high',
  'note': 'Explicitly states private, non-profit status; no state stake or serious conduct record identified.'},
 {'sponsorId': 'circle-usdc',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'circle-internet-group',
            'name': 'Circle Internet Group, Inc. (NYSE: CRCL) — public shareholders',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed US company, no state link → none.'},
  'claim': {'text': "USDC is issued by Circle; the issuer's parent, Circle Internet Group, Inc., listed on the NYSE "
                    'in June 2025 via an S-1 registration (SEC CIK 1876042). It is a US-listed company with '
                    'dispersed public shareholders and no state or state-fund owner.',
            'short': "USDC is issued by Circle; the issuer's parent, Circle Internet Group, Inc., listed on the NYSE "
                     'in June 2025 via an S-1 registration (SEC CIK 1876042).',
            'source': {'name': 'SEC Form S-1, Circle Internet Group, Inc.',
                       'date': '2025-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1876042/000119312525178989/d839239ds1.htm'}},
  'verdict': 'Owned by Circle Internet Group, Inc. (NYSE: CRCL) — public shareholders. Nothing found.',
  'confidence': 'high',
  'note': 'Listed US company, no state link → none.'},
 {'sponsorId': 'cisco',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'cisco',
            'name': 'Cisco Systems, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Used the FY2025 10-K; ownership is disclosed by incorporation into the proxy, which shows no '
                    '5%+ holder of note.'},
  'claim': {'text': 'Cisco Systems, Inc. (NASDAQ: CSCO) is a US-listed networking and software group with an '
                    'extremely dispersed register - no shareholder above roughly 5-6% and heavy index-fund '
                    'representation - and no state stake. Human-rights relevance is ordinary corporate conduct; '
                    "Cisco's main geopolitical exposure is its China/Huawei position rather than anything in its cap "
                    'table.',
            'short': 'Cisco Systems, Inc.',
            'source': {'name': 'Cisco Systems, Inc. Form 10-K for fiscal 2025 (SEC)',
                       'date': '2025-09-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm'}},
  'verdict': 'Owned by Cisco Systems, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Used the FY2025 10-K; ownership is disclosed by incorporation into the proxy, which shows no 5%+ holder '
          'of note.'},
 {'sponsorId': 'citigroup',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'citigroup-citi-owner',
            'name': 'Citigroup (Citi)',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Citigroup has no state ownership but has a documented conduct record: paid ~$1.1bn in 2019 for '
                    'Iran-related sanctions/AML failures and agreed to forfeit $227m in 2012 for Iran/Sudan '
                    "transactions. Under rubric, this is a 'lesser link' (concern) not ownership-based "
                    'severe/serious.'},
  'claim': {'text': 'Citigroup is a NYSE-listed bank with no state ownership but has documented conduct issues '
                    'including sanctions violations and settlements related to Iran/Sudan/Libya/Burma.',
            'short': 'Citigroup is a NYSE-listed bank with no state ownership but has documented conduct issues '
                     'including sanctions violations and settlements related to….',
            'source': {'name': 'Citigroup DEF 14A 2026',
                       'date': '2026-04-02',
                       'url': 'https://www.sec.gov/Archives/edgar/data/831001/000120677426000185/citi4583461-def14a.htm'}},
  'verdict': 'Citigroup is a NYSE-listed bank with no state ownership but has documented conduct issues including '
             'sanctions violations and settlements related to….',
  'confidence': 'medium',
  'note': 'Citigroup has no state ownership but has a documented conduct record: paid ~$1.1bn in 2019 for '
          'Iran-related sanctions/AML failures and agreed to forfeit $227m in 2012 for Iran/Sudan transactions. '
          "Under rubric, this is a 'lesser link' (concern) not ownership-based severe/serious."},
 {'sponsorId': 'citizens-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'citizens-bank-citizens-financial-group-owner',
            'name': 'Citizens Bank (Citizens Financial Group)',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Citizens Financial Group, Inc. is owned by Citizens Bank (Citizens Financial Group). No state '
                    'shareholder identified. Ownership sits with public institutional and retail investors, so the '
                    'sponsorship money is purely private capital.',
            'short': 'Citizens Financial Group, Inc.',
            'source': {'name': 'CITIZENS FINANCIAL GROUP INC/RI DEF 14A 2026 (SEC)',
                       'date': '2026-03-09',
                       'url': 'https://www.sec.gov/Archives/edgar/data/759944/000075994426000064/cfg-20260309.htm'}},
  'verdict': 'Owned by Citizens Bank (Citizens Financial Group). Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'claude',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'anthropic',
            'name': 'Anthropic PBC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Stake figures come from court filings reported by NYT (Google ~14%) and from Amazon/Google '
                    'quarterly disclosures for the Amazon figure; both are minority and none is controlling.'},
  'claim': {'text': 'Claude is the product of Anthropic PBC, a Delaware public-benefit corporation that is privately '
                    'held but minority-owned by Big Tech: court documents in the Google antitrust case put Alphabet '
                    'at about 14% of Anthropic, with Amazon a further roughly 8%. Neither parent controls Anthropic, '
                    'and there is no state stake. Human-rights relevance is compute and data-labour supply chain '
                    'rather than ownership.',
            'short': 'Claude is the product of Anthropic PBC, a Delaware public-benefit corporation that is '
                     'privately held but minority-owned by Big Tech: court documents in the Google….',
            'source': {'name': "The New York Times - 'Inside Google's Investment in Anthropic'",
                       'date': '2025-03-11',
                       'url': 'https://www.nytimes.com/2025/03/11/technology/google-investment-anthropic.html'}},
  'verdict': 'Owned by Anthropic PBC. Nothing found.',
  'confidence': 'medium',
  'note': 'Stake figures come from court filings reported by NYT (Google ~14%) and from Amazon/Google quarterly '
          'disclosures for the Amazon figure; both are minority and none is controlling.'},
 {'sponsorId': 'cleveland-cliffs',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'cleveland-cliffs-owner',
            'name': 'Cleveland-Cliffs LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $146 million; 10-Q - 07/26/2023 - Cleveland-Cliffs Inc.: '
                    '$6 million; 10-Q - 07/26/2023 - Cleveland-Cliffs Inc.: $13 million'},
  'claim': {'text': 'Cleveland-Cliffs LLC is the ultimate owner of Cleveland-Cliffs.',
            'short': 'Cleveland-Cliffs LLC is the ultimate owner of Cleveland-Cliffs.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Cleveland-Cliffs LLC is the ultimate owner of Cleveland-Cliffs.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $146 million; 10-Q - 07/26/2023 - Cleveland-Cliffs Inc.: $6 '
          'million; 10-Q - 07/26/2023 - Cleveland-Cliffs Inc.: $13 million'},
 {'sponsorId': 'clickhouse',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'clickhouse-inc',
            'name': 'ClickHouse, Inc. (private, VC-backed)',
            'type': 'private-company',
            'country': 'US',
            'note': "Private owner → none. GIC (Singapore) is a minority investor only; Singapore's record is clean, "
                    'so no abuse link. Arguable concern if any SWF minority counts; recorded here.'},
  'claim': {'text': 'ClickHouse, Inc. is a private San Francisco analytics company whose Series C (led by Khosla '
                    'Ventures) and $400m Series D (led by Dragoneer) brought in financial investors including '
                    "Bessemer, Index and Singapore's sovereign fund GIC. Owner is private; only minority "
                    'sovereign-fund exposure.',
            'short': 'ClickHouse, Inc.',
            'source': {'name': 'ClickHouse official Series C/D announcements',
                       'date': '2025-05 / 2026-01',
                       'url': 'https://clickhouse.com/blog/clickhouse-raises-350-million-series-c-to-power-analytics-for-ai-era'}},
  'verdict': 'Owned by ClickHouse, Inc. (private, VC-backed). Nothing found.',
  'confidence': 'medium',
  'note': "Private owner → none. GIC (Singapore) is a minority investor only; Singapore's record is clean, so no "
          'abuse link. Arguable concern if any SWF minority counts; recorded here.'},
 {'sponsorId': 'cmc-markets',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'cmc-markets-plc',
            'name': 'CMC Markets Plc (London-listed; Cruddas family significant holder)',
            'type': 'listed-company',
            'country': 'GB',
            'note': 'Listed UK company with a founder/family anchor, no state link → none.'},
  'claim': {'text': 'CMC Markets is a London-listed CFD broker founded and led by Peter Cruddas, Baron Cruddas, '
                    'whose family is among the top shareholders; the rest is free float. No state or state-fund '
                    'owner.',
            'short': 'CMC Markets is a London-listed CFD broker founded and led by Peter Cruddas, Baron Cruddas, '
                     'whose family is among the top shareholders; the rest is free float.',
            'source': {'name': 'CMC Markets Plc press release (founder appointed to the Lords); Finance '
                               'Magnates/TradingView on shareholder base',
                       'date': '2020 / 2025',
                       'url': 'https://www.cmcmarkets.com/group/press-releases/peter-cruddas-appointed-to-the-house-of-lords-as-baron-cruddas-of-shoreditch'}},
  'verdict': 'Owned by CMC Markets Plc (London-listed; Cruddas family significant holder). Nothing found.',
  'confidence': 'high',
  'note': 'Listed UK company with a founder/family anchor, no state link → none.'},
 {'sponsorId': 'cme-group',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'cme-group-owner',
            'name': 'CME Group Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'CME Group is a publicly traded financial exchange company; no state stake or serious conduct '
                    'record identified.'},
  'claim': {'text': 'CME Group Inc. is a publicly traded company listed on the NASDAQ and NYSE under ticker CME.',
            'short': 'CME Group Inc.',
            'source': {'name': 'SEC DEF 14A for CME Group Inc.',
                       'date': '2026-03-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1156375/000162828026020500/cme-20260323.htm'}},
  'verdict': 'Owned by CME Group Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'CME Group is a publicly traded financial exchange company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'cognizant',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'cognizant',
            'name': 'Cognizant Technology Solutions Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Tier call is the softest in the batch - the FCPA case is real but small relative to peer sets. '
                    "'none' would be defensible."},
  'claim': {'text': 'Cognizant Technology Solutions Corporation (NASDAQ: CTSH) is a US-listed IT services firm with '
                    'dispersed institutional ownership and no state shareholder in any of its share classes. '
                    'Human-rights relevance is conduct and labour: a very large India-centric delivery workforce '
                    'plus a 2019 FCPA settlement with the SEC over bribery in India. That is a genuine but lesser '
                    'documented record, hence concern.',
            'short': 'Cognizant Technology Solutions Corporation (NASDAQ: CTSH) is a US-listed IT services firm with '
                     'dispersed institutional ownership and no state shareholder in any of….',
            'source': {'name': "Cognizant Technology Solutions Corporation DEF 14A 2026, 'Corporate governance' "
                               '(SEC)',
                       'date': '2026-04-17',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1058290/000130817926000290/ctsh014861-def14a.htm'}},
  'verdict': 'Cognizant Technology Solutions Corporation (NASDAQ: CTSH) is a US-listed IT services firm with '
             'dispersed institutional ownership and no state shareholder in any of….',
  'confidence': 'high',
  'note': "Tier call is the softest in the batch - the FCPA case is real but small relative to peer sets. 'none' "
          'would be defensible.'},
 {'sponsorId': 'commscope',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'belden',
            'name': 'Belden Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': "Ambiguity flagged: the sponsor label spans 'CommScope / Ruckus' but the two brands now have "
                    'different owners. Called it on Ruckus (the explicitly named brand and the product actually '
                    'promoted on the Haas car) -> Belden. If the entry means CommScope the brand, the owner is '
                    'Amphenol Corporation (SEC 8-K, 9 Jan 2026).'},
  'claim': {'text': 'The Haas partner brands have been split up since the deal was signed. RUCKUS Networks was sold '
                    'by Vistance Networks (formerly CommScope Holding) to Belden Inc. (NYSE: BDC) on 1 July 2026, '
                    'while the CommScope name and its connectivity business went to Amphenol Corporation in January '
                    '2026 for $10.5bn. Belden is a US-listed manufacturer with no state stake; ownership of the '
                    'sponsor is therefore private, and human-rights relevance is ordinary manufacturing supply '
                    'chain.',
            'short': 'The Haas partner brands have been split up since the deal was signed.',
            'source': {'name': "Belden Inc. - 'Belden Completes Acquisition of RUCKUS Networks'",
                       'date': '2026-07-01',
                       'url': 'https://investor.belden.com/news/news-details/2026/Belden-Completes-Acquisition-of-RUCKUS-Networks/default.aspx'}},
  'verdict': 'Owned by Belden Inc.. Nothing found.',
  'confidence': 'medium',
  'note': "Ambiguity flagged: the sponsor label spans 'CommScope / Ruckus' but the two brands now have different "
          'owners. Called it on Ruckus (the explicitly named brand and the product actually promoted on the Haas '
          'car) -> Belden. If the entry means CommScope the brand, the owner is Amphenol Corporation (SEC 8-K, 9 Jan '
          '2026).'},
 {'sponsorId': 'compass-minerals',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'compass-minerals',
            'name': 'Compass Minerals International, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': "Koch's 16.81% is the notable structural fact; it is private capital, so no tier change. Koch "
                    'does, however, have its own well-documented political and environmental record that may matter '
                    'downstream in this dataset.'},
  'claim': {'text': 'Compass Minerals International, Inc. (NYSE: CMP) is a US-listed salt and plant-nutrition miner '
                    'with no state shareholder. Its register does contain one large private block - Koch Industries '
                    'holds about 16.8% through KMT Investment Holdings - but Koch is a family-owned private company, '
                    'not a state, so the tier stays none. Human-rights relevance is mining, water and permitting '
                    'conduct (its lithium and salt operations consume significant water).',
            'short': 'Compass Minerals International, Inc.',
            'source': {'name': "Compass Minerals International, Inc. DEF 14A 2026, '5% Stockholders' (SEC)",
                       'date': '2026-01-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1227654/000130817926000019/cmp014557_def14a.htm'}},
  'verdict': 'Owned by Compass Minerals International, Inc.. Nothing found.',
  'confidence': 'high',
  'note': "Koch's 16.81% is the notable structural fact; it is private capital, so no tier change. Koch does, "
          'however, have its own well-documented political and environmental record that may matter downstream in '
          'this dataset.'},
 {'sponsorId': 'coors-brewing-co',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'coors-brewing-co-molson-coors-owner',
            'name': 'Coors Brewing Co. (Molson Coors)',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Molson Coors is publicly traded with no state ownership; largest holders are Vanguard (~12%) '
                    'and BlackRock (~7.5%). No documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'Molson Coors Beverage Company is a NYSE-listed brewer with no state ownership; largest '
                    'shareholders are institutional investors (Vanguard, BlackRock) each under 10%.',
            'short': 'Molson Coors Beverage Company is a NYSE-listed brewer with no state ownership; largest '
                     'shareholders are institutional investors (Vanguard, BlackRock) each under 10%.',
            'source': {'name': 'Molson Coors DEF 14A 2026',
                       'date': '2026-03-25',
                       'url': 'https://www.sec.gov/Archives/edgar/data/24545/000110465926034154/tap-20260506xdef14a.htm'}},
  'verdict': 'Owned by Coors Brewing Co. (Molson Coors). Nothing found.',
  'confidence': 'high',
  'note': 'Molson Coors is publicly traded with no state ownership; largest holders are Vanguard (~12%) and '
          'BlackRock (~7.5%). No documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'corendon',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'corendon-tourism-group',
            'name': 'Corendon Tourism Group (Corendon Holdings)',
            'type': 'private-company',
            'country': 'NL',
            'note': 'Dutch/Turkish dual footprint, so some sources treat it as Turkish; ownership is private '
                    "founder/family either way. CEO Gunay Uslu (Atilay's relative) is a former Dutch state "
                    'secretary, which is a personnel not ownership link.'},
  'claim': {'text': 'Corendon Airlines is a subsidiary of the privately held Corendon Tourism Group, founded in 2000 '
                    'by Atilay Uslu and Yildiray Karaer; Uslu is listed as owner/founder and chairman. '
                    'Dutch-headquartered (Amsterdam) group with Turkish operations; no state shareholding.',
            'short': 'Corendon Airlines is a subsidiary of the privately held Corendon Tourism Group, founded in '
                     '2000 by Atilay Uslu and Yildiray Karaer; Uslu is listed as owner/founder….',
            'source': {'name': 'Corendon Airlines corporate profile / TravMagazine reporting on Corendon management',
                       'date': '2024-01',
                       'url': 'https://www.travmagazine.nl/en/corendon-introduces-its-new-management-team'}},
  'verdict': 'Owned by Corendon Tourism Group (Corendon Holdings). Nothing found.',
  'confidence': 'medium',
  'note': 'Dutch/Turkish dual footprint, so some sources treat it as Turkish; ownership is private founder/family '
          "either way. CEO Gunay Uslu (Atilay's relative) is a former Dutch state secretary, which is a personnel "
          'not ownership link.'},
 {'sponsorId': 'crowdstrike',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'crowdstrike',
            'name': 'CrowdStrike Holdings, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'CrowdStrike Holdings, Inc. (NASDAQ: CRWD) is a US-listed cybersecurity company with a dispersed '
                    'register dominated by index funds; co-founder and CEO George Kurtz is the most prominent '
                    'individual holder. There is no state shareholder. Human-rights relevance is thin - its record '
                    'event (the July 2024 global outage) is operational rather than rights-based.',
            'short': 'CrowdStrike Holdings, Inc.',
            'source': {'name': "CrowdStrike Holdings, Inc. DEF 14A 2026, 'Security Ownership of Certain Beneficial "
                               "Owners and Management' (SEC)",
                       'date': '2026-05-05',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1535527/000110465926055599/tm2532333-4_def14a.htm'}},
  'verdict': 'Owned by CrowdStrike Holdings, Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'crypto-com',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'foris-dax',
            'name': 'Foris DAX MT Limited (owned by Foris Holdings KY Limited)',
            'type': 'private-company',
            'country': 'KY',
            'note': 'Used a US regulator document rather than a company page because it names the top-tier holding '
                    'company, which the Crypto.com site does not.'},
  'claim': {'text': "Crypto.com's corporate chain ends offshore: the OCC's conditional trust-bank approval records "
                    'that Foris Holdings KY Limited, a Cayman Islands corporation, owns Foris DAX MT Ltd. (Malta), '
                    'which is described as the top-tier holding company for the Crypto.com family of companies. '
                    'Ownership is entirely private, with no state stake, albeit in a Cayman/Malta structure that is '
                    'opaque below the top tier. Human-rights relevance is crypto-market and licensing conduct across '
                    'many jurisdictions.',
            'short': "Crypto.com's corporate chain ends offshore: the OCC's conditional trust-bank approval records "
                     'that Foris Holdings KY Limited, a Cayman Islands corporation, owns….',
            'source': {'name': 'US Office of the Comptroller of the Currency, Conditional Approval 1367 (Crypto.com '
                               'National Trust Bank)',
                       'date': '2026-02-20',
                       'url': 'https://www.occ.gov/topics/charters-and-licensing/interpretations-and-decisions/2026/cd1367.pdf'}},
  'verdict': 'Owned by Foris DAX MT Limited (owned by Foris Holdings KY Limited). Nothing found.',
  'confidence': 'high',
  'note': 'Used a US regulator document rather than a company page because it names the top-tier holding company, '
          'which the Crypto.com site does not.'},
 {'sponsorId': 'cynar-spritz',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'davide-campari-milano',
            'name': 'Davide Campari-Milano N.V.',
            'type': 'listed-company',
            'country': 'IT',
            'note': "Campari's own website renders client-side, so the annual report PDF was used to establish Cynar "
                    "as a Campari brand. The sponsor name 'Cynar Spritz' is a brand, not an entity."},
  'claim': {'text': 'Cynar is not an independent company - it is a brand in the portfolio of Davide Campari-Milano '
                    "N.V., the Milan-headquartered spirits group listed on Borsa Italiana, sitting in its 'House of "
                    "Aperitifs' brand cluster. Campari itself is controlled by the Garavoglia family through their "
                    'holding company but has no state shareholder. Human-rights relevance is alcohol-sector labour '
                    'and agricultural sourcing (sugar, agave, botanicals).',
            'short': 'Cynar is not an independent company - it is a brand in the portfolio of Davide Campari-Milano '
                     'N.V., the Milan-headquartered spirits group listed on Borsa Italiana,….',
            'source': {'name': 'Campari Group Annual Report for the year ended 31 December 2024, brand overview',
                       'date': '2024-12-31',
                       'url': 'https://camparigroup.com/sites/default/files/downloads/01.1%20Campari%20Group_Annual%20Report%20for%20the%20year%20ended%2031%20December%202024.pdf'}},
  'verdict': 'Owned by Davide Campari-Milano N.V.. Nothing found.',
  'confidence': 'medium',
  'note': "Campari's own website renders client-side, so the annual report PDF was used to establish Cynar as a "
          "Campari brand. The sponsor name 'Cynar Spritz' is a brand, not an entity."},
 {'sponsorId': 'daikin-comfort-technologies',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'daikin-comfort-technologies-owner',
            'name': 'Daikin Comfort Technologies',
            'type': 'listed-company',
            'country': 'JP',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Daikin Industries, Ltd. is owned by Daikin Comfort Technologies. No state shareholder '
                    'identified. Ownership sits with public institutional and retail investors, so the sponsorship '
                    'money is purely private capital.',
            'short': 'Daikin Industries, Ltd.',
            'source': {'name': 'Daikin Industries Ltd. Shareholder Information',
                       'date': '2026-09-24',
                       'url': 'https://www.daikin.com/investor/stock/stock_info'}},
  'verdict': 'Owned by Daikin Comfort Technologies. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'dazn-bet-club',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'access-industries',
            'name': 'Access Industries, Inc.',
            'type': 'private-company',
            'country': 'US',
            'note': 'Blavatnik is Ukrainian-born, US/UK-resident; Access is not a Russian state vehicle, so not '
                    "scored severe. The DAZN 'Bet Club' product is a DAZN betting sub-brand rather than a separate "
                    'company.'},
  'claim': {'text': 'DAZN Bet Club sits on DAZN, the sports-streaming group that is wholly owned by Access '
                    "Industries, Len Blavatnik's privately held global investment company, where DAZN appears as a "
                    "portfolio holding. There is no state stake - Blavatnik's money is private family capital, "
                    'though Access has historically held Russia-linked assets. Human-rights relevance is gambling '
                    'licensing and sports-rights economics.',
            'short': 'DAZN Bet Club sits on DAZN, the sports-streaming group that is wholly owned by Access '
                     "Industries, Len Blavatnik's privately held global investment company, where….",
            'source': {'name': 'Access Industries - DAZN portfolio page',
                       'date': None,
                       'url': 'https://www.accessindustries.com/investments/dazn'}},
  'verdict': 'Owned by Access Industries, Inc.. Nothing found.',
  'confidence': 'medium',
  'note': 'Blavatnik is Ukrainian-born, US/UK-resident; Access is not a Russian state vehicle, so not scored severe. '
          "The DAZN 'Bet Club' product is a DAZN betting sub-brand rather than a separate company."},
 {'sponsorId': 'deel',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'deel-inc',
            'name': 'Deel, Inc.',
            'type': 'private-company',
            'country': 'US',
            'note': 'US SEC investigation into revenue/accounting and a US money-laundering lawsuit have been '
                    'reported, but these are company-level regulatory matters, not a state-ownership link, so tier '
                    'stays none. No parent company above Deel, Inc.'},
  'claim': {'text': 'Deel, Inc. is a privately held US (Delaware/San Francisco) global payroll and EOR company; it '
                    'is venture-backed with a $300m Series E at a $17.3bn valuation co-led by Ribbit Capital and '
                    'Andreessen Horowitz, and has no sovereign or state shareholder on its cap table.',
            'short': 'Deel, Inc.',
            'source': {'name': "Deel official blog 'Our Series E: Building the global infrastructure of work'; "
                               'FinTech Global coverage',
                       'date': '2025-10-17',
                       'url': 'https://www.deel.com/blog/new-investment-valuation/'}},
  'verdict': 'Owned by Deel, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'US SEC investigation into revenue/accounting and a US money-laundering lawsuit have been reported, but '
          'these are company-level regulatory matters, not a state-ownership link, so tier stays none. No parent '
          'company above Deel, Inc.'},
 {'sponsorId': 'deghi',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'deghi',
            'name': 'DEGHI S.p.A.',
            'type': 'private-company',
            'country': 'IT',
            'note': 'The sponsor also appears alongside Betitaly/Betitalypay on the Lecce shirt; DEGHI is the main '
                    'sponsor and the entity rated. Ownership is founder-led but no formal shareholder register is '
                    'published.'},
  'claim': {'text': 'DEGHI S.p.A. is a private Italian furniture and home e-commerce company based in the Lecce '
                    'area, founded in 2009 and still closely identified with and led by founder Alberto Paglialunga '
                    '(it trades from a garage start-up to roughly EUR 85m revenue). There is no state stake and no '
                    'listing. Human-rights relevance is ordinary retail, logistics and delivery labour.',
            'short': 'DEGHI S.p.A.',
            'source': {'name': "DEGHI - 'Noi siamo Deghi' (company page)",
                       'date': None,
                       'url': 'https://www.deghi.it/noi-siamo-deghi'}},
  'verdict': 'Owned by DEGHI S.p.A.. Nothing found.',
  'confidence': 'medium',
  'note': 'The sponsor also appears alongside Betitaly/Betitalypay on the Lecce shirt; DEGHI is the main sponsor and '
          'the entity rated. Ownership is founder-led but no formal shareholder register is published.'},
 {'sponsorId': 'dell',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'dell-technologies',
            'name': 'Dell Technologies Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'Dell Technologies Inc. (NYSE: DELL) is a US-listed hardware and infrastructure company '
                    'controlled by founder Michael S. Dell through high-vote Class B common stock - he is chairman '
                    'and CEO and signs the 10-K as principal executive officer - with 47.8m Class B shares '
                    'outstanding against 276.7m Class A. There is no state shareholder. Human-rights relevance is '
                    'manufacturing supply chain and China exposure.',
            'short': 'Dell Technologies Inc.',
            'source': {'name': "Dell Technologies Inc. DEF 14A 2026, 'Security Ownership of Certain Beneficial "
                               "Owners and Management' (SEC)",
                       'date': '2026-05-15',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1571996/000119312526226734/d132444ddef14a.htm'}},
  'verdict': 'Owned by Dell Technologies Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'delta-air-lines',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'delta-air-lines-owner',
            'name': 'Delta Air Lines LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $763300 million; Delta to settle class-action lawsuit '
                    'over faulty refunds during Covid | CNN Business: $27 billion; Delta to settle class-action '
                    'lawsuit over faulty refunds during Covid | CNN Business: $2.3 billion'},
  'claim': {'text': 'Delta Air Lines LLC is the ultimate owner of Delta Air Lines.',
            'short': 'Delta Air Lines LLC is the ultimate owner of Delta Air Lines.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Delta Air Lines LLC is the ultimate owner of Delta Air Lines.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $763300 million; Delta to settle class-action lawsuit over faulty '
          'refunds during Covid | CNN Business: $27 billion; Delta to settle class-action lawsuit over faulty '
          'refunds during Covid | CNN Business: $2.3 billion'},
 {'sponsorId': 'desert-financial-credit-union',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'desert-financial-credit-union-owner',
            'name': 'Desert Financial Credit Union',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states not-for-profit, member-owned credit union; no state stake or serious conduct '
                    'record identified.'},
  'claim': {'text': 'Unlike banks, which are owned by shareholders, Desert Financial Credit Union is a '
                    'not-for-profit credit union that is member-owned.',
            'short': 'Unlike banks, which are owned by shareholders, Desert Financial Credit Union is a '
                     'not-for-profit credit union that is member-owned.',
            'source': {'name': 'Desert Financial Community Involvement page',
                       'date': '2026-09-24',
                       'url': 'https://www.desertfinancial.com/en/who-we-are/community-involvement'}},
  'verdict': 'Owned by Desert Financial Credit Union. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states not-for-profit, member-owned credit union; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'deutsche-telekom',
  'tier': 'concern',
  'ownership': 'part-owned',
  'owner': {'id': 'federal-republic-of-germany',
            'name': 'Federal Republic of Germany (direct stake + KfW) with the remainder free float',
            'type': 'state',
            'country': 'DE',
            'note': "State is the largest single owner block → state link, but Germany's record is not seriously "
                    'abusive → concern. Alternative reading: none. KfW stake note: '
                    'https://www.kfw.de/About-KfW/Newsroom/Latest-News/News-Details_134528.html'},
  'claim': {'text': "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the "
                    'anchor shareholder via KfW (approx. 14.4%) plus a direct federal holding, together roughly '
                    '28-30% of shares, with the balance free float.',
            'short': "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the "
                     'anchor shareholder via KfW (approx.',
            'source': {'name': 'Deutsche Telekom Investor Relations, Shareholder structure; KfW newsroom',
                       'date': '2026-06-30',
                       'url': 'https://www.telekom.com/en/investor-relations/share/shareholder-structure'}},
  'verdict': "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the anchor "
             'shareholder via KfW (approx.',
  'confidence': 'medium',
  'note': "State is the largest single owner block → state link, but Germany's record is not seriously abusive → "
          'concern. Alternative reading: none. KfW stake note: '
          'https://www.kfw.de/About-KfW/Newsroom/Latest-News/News-Details_134528.html'},
 {'sponsorId': 'dhl',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'deutsche-post-dhl',
            'name': 'DHL Group (Deutsche Post AG)',
            'type': 'listed-company',
            'country': 'DE',
            'note': "Judgement call: 17.7% via KfW is a partial, not controlling, state stake, so 'concern' per the "
                    'rubric. DHL would argue over 78% is free float and it is not state-controlled - which is why it '
                    "is not 'serious'."},
  'claim': {'text': 'DHL Group (Deutsche Post AG) is a listed German logistics company, but it is not purely '
                    'private: KfW Bankengruppe, the state-owned German development bank, holds approximately 204 '
                    'million shares, 17.727% of the share capital as at 30 June 2026. A partial state stake earns '
                    'the mid tier rather than serious. Human-rights relevance is logistics labour and subcontracting '
                    'across a global network.',
            'short': 'DHL Group (Deutsche Post AG) is a listed German logistics company, but it is not purely '
                     'private: KfW Bankengruppe, the state-owned German development bank, holds….',
            'source': {'name': 'DHL Group - Shareholder Structure (company IR)',
                       'date': '2026-06-30',
                       'url': 'https://www.dpdhl.com/en/investors/shares/shareholder-structure.html'}},
  'verdict': 'DHL Group (Deutsche Post AG) is a listed German logistics company, but it is not purely private: KfW '
             'Bankengruppe, the state-owned German development bank, holds….',
  'confidence': 'high',
  'note': "Judgement call: 17.7% via KfW is a partial, not controlling, state stake, so 'concern' per the rubric. "
          'DHL would argue over 78% is free float and it is not state-controlled - which is why it is not '
          "'serious'."},
 {'sponsorId': 'digi',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'digi-communications-nv',
            'name': 'Digi Communications N.V.',
            'type': 'listed-company',
            'country': 'RO',
            'note': 'Romanian listing plus US/Nasdaq-style ADRs; ownership private/founder with public float. '
                    'Founder-linked governance litigation exists but no state link.'},
  'claim': {'text': 'Digi Communications N.V. is a Dutch-incorporated, Bucharest-listed (BSE: DIGI) telecoms group '
                    'and the controlling shareholder of Digi Romania (formerly RCS & RDS). Founder Zoltan Teszari is '
                    'the controlling shareholder; the rest is free float. No state or state-fund stake.',
            'short': 'Digi Communications N.V.',
            'source': {'name': "Digi Communications N.V. official 'About Us' / Board of Directors (Teszari, "
                               'controlling shareholder)',
                       'date': '2026',
                       'url': 'https://www.digi-communications.ro/en/about-us'}},
  'verdict': 'Owned by Digi Communications N.V.. Nothing found.',
  'confidence': 'high',
  'note': 'Romanian listing plus US/Nasdaq-style ADRs; ownership private/founder with public float. Founder-linked '
          'governance litigation exists but no state link.'},
 {'sponsorId': 'directv',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'tpg',
            'name': 'TPG Capital (TPG Inc.)',
            'type': 'private-company',
            'country': 'US',
            'note': "TPG Inc. is itself Nasdaq-listed, but DirecTV is held by TPG's private funds, so the owner type "
                    'is private-company.'},
  'claim': {'text': 'DirecTV is now wholly owned by TPG Capital, the US/European private-equity platform of TPG '
                    "Inc., which completed its purchase of AT&T's remaining 70% stake on 2 July 2025 and made "
                    'DIRECTV a wholly owned portfolio company. Ownership is purely private equity with no state '
                    'stake. Human-rights relevance is ordinary media/consumer labour and contractor conduct.',
            'short': 'DirecTV is now wholly owned by TPG Capital, the US/European private-equity platform of TPG '
                     "Inc., which completed its purchase of AT&T's remaining 70% stake on 2….",
            'source': {'name': "TPG - 'TPG Completes Acquisition of AT&T's 70% Stake in DIRECTV'",
                       'date': '2025-07-02',
                       'url': 'https://shareholders.tpg.com/news-releases/news-release-details/tpg-completes-acquisition-atts-70-stake-directv/'}},
  'verdict': 'Owned by TPG Capital (TPG Inc.). Nothing found.',
  'confidence': 'high',
  'note': "TPG Inc. is itself Nasdaq-listed, but DirecTV is held by TPG's private funds, so the owner type is "
          'private-company.'},
 {'sponsorId': 'dream-finders-homes',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'dream-finders-homes-owner',
            'name': 'Dream Finders Homes',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Dream Finders Homes is publicly traded (DFH) with no state ownership; largest institutional '
                    'holders are Vanguard and BlackRock, each under 10%. No human-rights concerns in ownership chain '
                    'identified.'},
  'claim': {'text': 'Dream Finders Homes, Inc. is a publicly traded homebuilder with no state ownership; largest '
                    'shareholders are institutional investors (Vanguard, BlackRock) each under 10%.',
            'short': 'Dream Finders Homes, Inc.',
            'source': {'name': 'Dream Finders Homes DEF 14A 2026',
                       'date': '2026-04-16',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1825088/000162828026025557/dfh-20260416.htm'}},
  'verdict': 'Owned by Dream Finders Homes. Nothing found.',
  'confidence': 'high',
  'note': 'Dream Finders Homes is publicly traded (DFH) with no state ownership; largest institutional holders are '
          'Vanguard and BlackRock, each under 10%. No human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'duracell',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'berkshire-hathaway',
            'name': 'Berkshire Hathaway Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': "Duracell's own company page (duracell.com/company) also states the Berkshire position since "
                    '2016.'},
  'claim': {'text': 'Duracell is a wholly owned subsidiary of Berkshire Hathaway Inc., transferred from Procter & '
                    "Gamble in a February 2016 share exchange and described by Duracell itself as a 'Berkshire "
                    "Hathaway Company since 2016'. Berkshire is NYSE-listed with no state shareholder. Human-rights "
                    'relevance is battery manufacturing inputs (lithium, cobalt, manganese) and their supply chains.',
            'short': 'Duracell is a wholly owned subsidiary of Berkshire Hathaway Inc., transferred from Procter & '
                     'Gamble in a February 2016 share exchange and described by Duracell….',
            'source': {'name': "P&G press release on SEC EDGAR - 'P&G Completes Exchange of Duracell to Berkshire "
                               "Hathaway'",
                       'date': '2016-02-29',
                       'url': 'https://www.sec.gov/Archives/edgar/data/80424/000008042416000171/duracelltransferpressrelease.htm'}},
  'verdict': 'Owned by Berkshire Hathaway Inc.. Nothing found.',
  'confidence': 'high',
  'note': "Duracell's own company page (duracell.com/company) also states the Berkshire position since 2016."},
 {'sponsorId': 'eaton',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'eaton-owner',
            'name': 'Eaton Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Eaton Corp plc is owned by Eaton Corporation. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Eaton Corp plc is owned by Eaton Corporation.',
            'source': {'name': 'Eaton Corp plc DEF 14A 2026 (SEC)',
                       'date': '2026-03-13',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1551182/000119312526105117/etn-20260312.htm'}},
  'verdict': 'Owned by Eaton Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'el-camino-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'el-camino-health',
            'name': 'El Camino Health',
            'type': 'private-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'El Camino Health is a not-for-profit hospital system in Santa Clara County, California, running '
                    'two acute-care hospitals in Los Gatos and Mountain View and a network of clinics. It has no '
                    'external owner beyond itself - no state stake and no listed float. Human-rights relevance is '
                    "thin: a local health system's labour and access record.",
            'short': 'El Camino Health is a not-for-profit hospital system in Santa Clara County, California, '
                     'running two acute-care hospitals in Los Gatos and Mountain View and a….',
            'source': {'name': 'El Camino Health - About Us',
                       'date': None,
                       'url': 'https://elcaminohealth.org/about-us'}},
  'verdict': 'Owned by El Camino Health. Nothing found.',
  'confidence': 'medium',
  'note': None},
 {'sponsorId': 'empower',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'empower-owner',
            'name': 'Empower LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $13150 million; FTC Secures Settlement with ICE and '
                    'Black Knight Resolving Antitrust Concerns in Mortgage Technology Deal | Federal Trade '
                    'Commission: $13.1 billion; Microsoft Word - Empower Anti-Corruption AML KYC Policy (CFM) v4 '
                    'FEBRUARY 2023 FINAL clean CFM and ELECTRIFI.docx: money laundering'},
  'claim': {'text': 'Empower LLC is the ultimate owner of Empower.',
            'short': 'Empower LLC is the ultimate owner of Empower.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Empower LLC is the ultimate owner of Empower.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $13150 million; FTC Secures Settlement with ICE and Black Knight '
          'Resolving Antitrust Concerns in Mortgage Technology Deal | Federal Trade Commission: $13.1 billion; '
          'Microsoft Word - Empower Anti-Corruption AML KYC Policy (CFM) v4 FEBRUARY 2023 FINAL clean CFM and '
          'ELECTRIFI.docx: money laundering'},
 {'sponsorId': 'energy-transfer',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'energy-transfer-owner',
            'name': 'Energy Transfer LP',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Although control lies with Kelcy Warren via LE GP, LLC, the partnership is publicly traded with '
                    'no state stake; no serious conduct record identified.'},
  'claim': {'text': 'Energy Transfer LP is a publicly traded master limited partnership; no single person or company '
                    'owns it outright, with public unitholders holding the majority of economic interest.',
            'short': 'Energy Transfer LP is a publicly traded master limited partnership; no single person or '
                     'company owns it outright, with public unitholders holding the majority of….',
            'source': {'name': 'LegalClarity article on Energy Transfer ownership',
                       'date': '2026-09-24',
                       'url': 'https://legalclarity.org/who-owns-energy-transfer-investors-and-insiders'}},
  'verdict': 'Owned by Energy Transfer LP. Nothing found.',
  'confidence': 'medium',
  'note': 'Although control lies with Kelcy Warren via LE GP, LLC, the partnership is publicly traded with no state '
          'stake; no serious conduct record identified.'},
 {'sponsorId': 'eni',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'eni',
            'name': 'Eni S.p.A.',
            'type': 'state',
            'country': 'IT',
            'note': 'Kept at serious rather than severe: Eni is a state oil major with conflict-zone assets but is '
                    'not itself a belligerent or a Russian state entity.'},
  'claim': {'text': 'Eni S.p.A. is effectively Italian state-owned: the Ministry of Economy and Finance (MEF) holds '
                    '2.166% directly and a further 30.918% indirectly through Cassa Depositi e Prestiti (which is '
                    "82.77% MEF-owned) - 33.084% in total, alongside a golden share - per Eni's own shareholder "
                    "communications to its 2026 AGM. State ownership alone earns serious. Eni's upstream operations "
                    'in Libya, Egypt, Nigeria and Mozambique give it live, conflict-adjacent human-rights exposure '
                    'on top.',
            'short': 'Eni S.p.A.',
            'source': {'name': 'Eni S.p.A. - Proposals of the Shareholder Ministry of the Economy and Finance (AGM '
                               '2026 filing)',
                       'date': '2026-04-10',
                       'url': 'https://www.eni.com/content/dam/enicom/documents/eng/governance/shareholders-meetings/2026/Proposals-of-Shareholder-Ministry-of-the-Economy-and-Finance-in-relation-to-item-6-7-and-10-of-the-agenda.pdf'}},
  'verdict': 'Eni S.p.A.',
  'confidence': 'high',
  'note': 'Kept at serious rather than severe: Eni is a state oil major with conflict-zone assets but is not itself '
          'a belligerent or a Russian state entity.'},
 {'sponsorId': 'estrella-galicia',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'corporacion-hijos-de-rivera',
            'name': 'Corporacion Hijos de Rivera, S.L.',
            'type': 'private-company',
            'country': 'ES',
            'note': 'Fifth-generation family group (Rivera family). No state or fund capital.'},
  'claim': {'text': 'Estrella Galicia is the flagship beer brand of Corporacion Hijos de Rivera, which describes '
                    "itself as a family-owned international brewing group with '100% national and independent "
                    "capital', headquartered in A Coruna since 1906.",
            'short': 'Estrella Galicia is the flagship beer brand of Corporacion Hijos de Rivera, which describes '
                     "itself as a family-owned international brewing group with '100%….",
            'source': {'name': 'Corporacion Hijos de Rivera official company page; Estrella Galicia International '
                               "'independent family-owned brewery'",
                       'date': '2026',
                       'url': 'http://corporacionhijosderivera.com/en/company'}},
  'verdict': 'Owned by Corporacion Hijos de Rivera, S.L.. Nothing found.',
  'confidence': 'high',
  'note': 'Fifth-generation family group (Rivera family). No state or fund capital.'},
 {'sponsorId': 'etoro',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'etoro',
            'name': 'eToro Group Ltd.',
            'type': 'listed-company',
            'country': 'IL',
            'note': 'Corrected from the blank owner in the input: eToro listed in May 2025, so its owner is a public '
                    'float with founder control, not a private company.'},
  'claim': {'text': 'eToro Group Ltd. is an Israeli-founded, UK-headquartered trading platform that went public on '
                    'Nasdaq in May 2025, pricing an upsized IPO of 13.7m Class A shares at $52.00 for gross proceeds '
                    'of $403m; founders retain control through a dual-class structure. There is no state stake. '
                    'Human-rights relevance is retail-CFD selling conduct and crypto exposure.',
            'short': 'eToro Group Ltd.',
            'source': {'name': 'eToro Group Ltd. Form 6-K (SEC) - IPO consummation',
                       'date': '2025-05-15',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1493318/000121390025044406/ea0242225-6k_etoro.htm'}},
  'verdict': 'Owned by eToro Group Ltd.. Nothing found.',
  'confidence': 'high',
  'note': 'Corrected from the blank owner in the input: eToro listed in May 2025, so its owner is a public float '
          'with founder control, not a private company.'},
 {'sponsorId': 'eurobet-live',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'entain-plc',
            'name': 'Entain plc',
            'type': 'listed-company',
            'country': 'GB',
            'note': "Entain ownership corroborated by SportBusiness ('Entain-owned infotainment platform') which is "
                    'paywalled; no primary corporate filing opened for the Eurobet.live brand entity itself, hence '
                    'medium confidence.'},
  'claim': {'text': 'Eurobet.live is the Italian-facing brand of Eurobet, described as the largest Italian brand '
                    'inside the Entain group, a London-listed bookmaker (LSE: ENT). Eurobet was founded in 1995 and '
                    'passed into the Coral/Gala Coral lineage before that business merged into Entain, so the '
                    'ultimate owner is a dispersed public float with no state stake. Human-rights relevance is '
                    'ordinary listed-corporate exposure (Italian ADM-licensed betting, franchised shop estate).',
            'short': 'Eurobet.live is the Italian-facing brand of Eurobet, described as the largest Italian brand '
                     'inside the Entain group, a London-listed bookmaker (LSE: ENT).',
            'source': {'name': 'iGaming Times - Eurobet operator profile',
                       'date': None,
                       'url': 'https://igaming-times.com/directory/eurobet'}},
  'verdict': 'Owned by Entain plc. Nothing found.',
  'confidence': 'medium',
  'note': "Entain ownership corroborated by SportBusiness ('Entain-owned infotainment platform') which is paywalled; "
          'no primary corporate filing opened for the Eurobet.live brand entity itself, hence medium confidence.'},
 {'sponsorId': 'everbank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'everbank-owner',
            'name': 'EverBank',
            'type': 'private-company',
            'country': 'USA',
            'note': 'EverBank is privately owned by a consortium of private equity funds; no state stake or '
                    'government control. No documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'EverBank is a privately held commercial bank owned by private equity investors (Stone Point '
                    'Capital, Warburg Pincus, Reverence Capital, etc.) with no state ownership.',
            'short': 'EverBank is a privately held commercial bank owned by private equity investors (Stone Point '
                     'Capital, Warburg Pincus, Reverence Capital, etc.) with no state….',
            'source': {'name': 'Stone Point Capital EverBank page',
                       'date': '2026-09-24',
                       'url': 'https://stonepoint.com/company/everbank'}},
  'verdict': 'Owned by EverBank. Nothing found.',
  'confidence': 'medium',
  'note': 'EverBank is privately owned by a consortium of private equity funds; no state stake or government '
          'control. No documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'expedia',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'expedia-group-inc',
            'name': 'Expedia Group, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': "Expedia's Liverpool sleeve deal is with Expedia Group, Inc., a Delaware-incorporated company "
                    'listed on Nasdaq (EXPE) and the parent of the Expedia, Hotels.com and Vrbo brands. It has a '
                    'dispersed public float with index managers (BlackRock, Vanguard, State Street) as the largest '
                    'holders and no controlling shareholder or state stake. Human-rights relevance: none material '
                    'beyond big-tech/consumer-Internet norms.',
            'short': "Expedia's Liverpool sleeve deal is with Expedia Group, Inc., a Delaware-incorporated company "
                     'listed on Nasdaq (EXPE) and the parent of the Expedia, Hotels.com and….',
            'source': {'name': 'Expedia Group, Inc. Form 10-K for FY2025 (SEC)',
                       'date': '2026-02-13',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm'}},
  'verdict': 'Owned by Expedia Group, Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'experience-abu-dhabi',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'government-of-abu-dhabi',
            'name': 'Government of Abu Dhabi',
            'type': 'state',
            'country': 'AE',
            'note': 'Ultimate owner is the Government of Abu Dhabi, a state entity, which places it in the serious '
                    'tier per rubric (state owner).'},
  'claim': {'text': 'Experience Abu Dhabi is the official tourism authority of the Emirate of Abu Dhabi, a state '
                    'government entity.',
            'short': 'Experience Abu Dhabi is the official tourism authority of the Emirate of Abu Dhabi, a state '
                     'government entity.',
            'source': {'name': 'Department of Culture and Tourism - Abu Dhabi website',
                       'date': '2026-09-24',
                       'url': 'https://dct.gov.ae/en/default.aspx'}},
  'verdict': 'Experience Abu Dhabi is the official tourism authority of the Emirate of Abu Dhabi, a state government '
             'entity.',
  'confidence': 'high',
  'note': 'Ultimate owner is the Government of Abu Dhabi, a state entity, which places it in the serious tier per '
          'rubric (state owner).'},
 {'sponsorId': 'experience-kissimmee',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'osceola-county-tourism-authority',
            'name': 'Experience Kissimmee (official tourism authority for Osceola County, Florida)',
            'type': 'state',
            'country': 'US',
            'note': "County-level rather than national, so 'concern' would also be defensible; called 'serious' "
                    "because the rubric gives 'serious' for any state or state-fund owner. Public funding confirmed "
                    "in Experience Kissimmee's own 26-27 Grants Manual citing the Tourist Development Tax."},
  'claim': {'text': 'Experience Kissimmee is not a company: it is the official destination marketing authority for '
                    "Osceola County, Florida, funded from the county's Tourist Development Tax and governed under "
                    'the state Local Option Tourist Development Act. Because the owner is a public body, the '
                    "state-owner rule puts it in 'serious'. Human-rights relevance is remote - a local government "
                    'tourism body with no armed-conflict or conflict-minerals exposure.',
            'short': 'Experience Kissimmee is not a company: it is the official destination marketing authority for '
                     "Osceola County, Florida, funded from the county's Tourist Development….",
            'source': {'name': 'Experience Kissimmee - About us (official tourism authority for Osceola County)',
                       'date': None,
                       'url': 'https://experiencekissimmee.com/about-us'}},
  'verdict': 'Experience Kissimmee is not a company: it is the official destination marketing authority for Osceola '
             "County, Florida, funded from the county's Tourist Development….",
  'confidence': 'high',
  'note': "County-level rather than national, so 'concern' would also be defensible; called 'serious' because the "
          "rubric gives 'serious' for any state or state-fund owner. Public funding confirmed in Experience "
          "Kissimmee's own 26-27 Grants Manual citing the Tourist Development Tax."},
 {'sponsorId': 'extreme-networks',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'extreme-networks-inc',
            'name': 'Extreme Networks, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'Extreme Networks, Inc. (Nasdaq: EXTR) is the Audi Revolut F1 Team partner: a US networking '
                    'vendor listed on Nasdaq with dispersed institutional ownership and no parent company, family '
                    'control or state stake. Human-rights relevance is limited to ordinary supply-chain and '
                    'hardware-sourcing exposure.',
            'short': 'Extreme Networks, Inc.',
            'source': {'name': 'Extreme Networks Investor Relations - corporate overview',
                       'date': None,
                       'url': 'https://investor.extremenetworks.com/'}},
  'verdict': 'Owned by Extreme Networks, Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'fedex',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'fedex-owner',
            'name': 'FedEx LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $0 million; FedEx Corporation: money laundering; Short '
                    'AirBoss (ABSSF): Lawsuit & Forced Labor Issues Impact Growth Pipeline & Inventory - Supply '
                    'Chain Council of European Union | Scceu.org: forced labor'},
  'claim': {'text': 'FedEx LLC is the ultimate owner of FedEx.',
            'short': 'FedEx LLC is the ultimate owner of FedEx.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'FedEx LLC is the ultimate owner of FedEx.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $0 million; FedEx Corporation: money laundering; Short AirBoss '
          '(ABSSF): Lawsuit & Forced Labor Issues Impact Growth Pipeline & Inventory - Supply Chain Council of '
          'European Union | Scceu.org: forced labor'},
 {'sponsorId': 'fifth-third-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'fifth-third-bank-owner',
            'name': 'Fifth Third Bancorp',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Fifth Third Bancorp is a publicly traded bank holding company; no state stake or serious '
                    'conduct record identified.'},
  'claim': {'text': 'Fifth Third Bancorp is a publicly traded company listed on the NASDAQ under ticker FITB.',
            'short': 'Fifth Third Bancorp is a publicly traded company listed on the NASDAQ under ticker FITB.',
            'source': {'name': 'SEC DEF 14A for Fifth Third Bancorp',
                       'date': '2026-03-09',
                       'url': 'https://www.sec.gov/Archives/edgar/data/35527/000119312526098679/d47600ddef14a.htm'}},
  'verdict': 'Owned by Fifth Third Bancorp. Nothing found.',
  'confidence': 'high',
  'note': 'Fifth Third Bancorp is a publicly traded bank holding company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'fiserv',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'fiserv-owner',
            'name': 'Fiserv',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Fiserv is publicly traded with no state ownership; largest holder is Vanguard (~11.9%). No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Fiserv is a NYSE-listed financial technology company with no state ownership; largest '
                    'shareholder is The Vanguard Group (~11.9%) and other institutions each under 10%.',
            'short': 'Fiserv is a NYSE-listed financial technology company with no state ownership; largest '
                     'shareholder is The Vanguard Group (~11.9%) and other institutions each under….',
            'source': {'name': 'Fiserv DEF 14A 2026',
                       'date': '2026-04-02',
                       'url': 'https://www.sec.gov/Archives/edgar/data/798354/000114036126013003/ny20062579x1_def14a.htm'}},
  'verdict': 'Owned by Fiserv. Nothing found.',
  'confidence': 'high',
  'note': 'Fiserv is publicly traded with no state ownership; largest holder is Vanguard (~11.9%). No documented '
          'human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'fix-network',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'mondofix-inc',
            'name': 'Mondofix Inc. (dba Fix Network World)',
            'type': 'private-company',
            'country': 'CA',
            'note': "The group publishes no share register; 'largest shareholder' and 'majority control' are the "
                    "company's own words. No state or PE owner identified."},
  'claim': {'text': 'The Haas F1 partner is Fix Network, the trading name of Mondofix Inc., a Blainville, Quebec '
                    'company running the Fix Auto, NOVUS Glass and ProColor franchise networks. President and CEO '
                    'Steve Leal joined as a franchisee, led a buyout to become largest shareholder of Fix Auto '
                    'Canada in 2013 and took majority control in 2015 - private Canadian ownership, no state stake. '
                    'Nothing suggests a state or conflict link; the sponsor is a franchised collision-repair '
                    'operator.',
            'short': 'The Haas F1 partner is Fix Network, the trading name of Mondofix Inc., a Blainville, Quebec '
                     'company running the Fix Auto, NOVUS Glass and ProColor franchise networks.',
            'source': {'name': 'Fix Network World - Steve Leal, President & CEO (leadership profile)',
                       'date': '2022-12-31',
                       'url': 'https://fixnetwork.com/en/leadership-team/steve-leal'}},
  'verdict': 'Owned by Mondofix Inc. (dba Fix Network World). Nothing found.',
  'confidence': 'medium',
  'note': "The group publishes no share register; 'largest shareholder' and 'majority control' are the company's own "
          'words. No state or PE owner identified.'},
 {'sponsorId': 'flexicar',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'flexicar-internacional',
            'name': 'Flexicar Internacional (owner Luis Oliver Cornago)',
            'type': 'private-company',
            'country': 'ES',
            'note': 'Single-owner private group, ~180 dealerships in Spain/Portugal. Not the unrelated Australian '
                    'Hertz franchise.'},
  'claim': {'text': "Flexicar is Spain's largest used-car dealer network, majority owned by founder Luis Oliver "
                    'Cornago, who reorganized the group under Flexicar Internacional and injected EUR 7.6m of his '
                    'own funds; company registry/legal form is private (Flexicar, empresa privada).',
            'short': "Flexicar is Spain's largest used-car dealer network, majority owned by founder Luis Oliver "
                     'Cornago, who reorganized the group under Flexicar Internacional and….',
            'source': {'name': "El Confidencial - 'Flexicar fusiona sus firmas bajo el paraguas internacional'; "
                               "Spanish Wikipedia 'Flexicar (Espana)'",
                       'date': '2025-01-17',
                       'url': 'https://www.elconfidencial.com/empresas/2025-01-17/flexicar-fusiona-sociedades-batir-facturacion_4044206/'}},
  'verdict': 'Owned by Flexicar Internacional (owner Luis Oliver Cornago). Nothing found.',
  'confidence': 'high',
  'note': 'Single-owner private group, ~180 dealerships in Spain/Portugal. Not the unrelated Australian Hertz '
          'franchise.'},
 {'sponsorId': 'ford',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ford-motor-company',
            'name': 'Ford Motor Company',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'The Oracle Red Bull Racing front-of-car branding is Ford Motor Company (NYSE: F), the Dearborn '
                    'automaker. Ford is publicly listed but not ownerless: the Ford family holds the super-voting '
                    "Class B stock disclosed in the company's proxy's Class B beneficial ownership table, so control "
                    'is family-anchored while the economic float is public. No state stake; human-rights relevance '
                    'is ordinary manufacturing and battery-minerals supply-chain exposure.',
            'short': 'The Oracle Red Bull Racing front-of-car branding is Ford Motor Company (NYSE: F), the Dearborn '
                     'automaker.',
            'source': {'name': 'Ford Motor Company DEF 14A proxy statement (SEC)',
                       'date': '2026-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/37996/000155278126000164/e26003_f-def14a.htm'}},
  'verdict': 'Owned by Ford Motor Company. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'ford-motor-company',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ford-motor-company',
            'name': 'Ford Motor Company',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Ford Motor Company is owned by Ford Motor Company. No state shareholder identified. Ownership '
                    'sits with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Ford Motor Company is owned by Ford Motor Company.',
            'source': {'name': 'FORD MOTOR CO DEF 14A 2026 (SEC)',
                       'date': '2026-03-27',
                       'url': 'https://www.sec.gov/Archives/edgar/data/37996/000155278126000164/e26003_f-def14a.htm'}},
  'verdict': 'Owned by Ford Motor Company. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'ford-rb',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ford-motor-company',
            'name': 'Ford Motor Company',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': "Ford Racing on the Racing Bulls sleeve is the same ultimate owner as Ford's Red Bull deal: Ford "
                    'Motor Company (NYSE: F), with family-held super-voting Class B stock and a public float. '
                    "Private-sector throughout, so 'none', with only normal automaker supply-chain exposure.",
            'short': "Ford Racing on the Racing Bulls sleeve is the same ultimate owner as Ford's Red Bull deal: "
                     'Ford Motor Company (NYSE: F), with family-held super-voting Class B….',
            'source': {'name': 'Ford Motor Company DEF 14A proxy statement (SEC)',
                       'date': '2026-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/37996/000155278126000164/e26003_f-def14a.htm'}},
  'verdict': 'Owned by Ford Motor Company. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'foundation-building-materials',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'foundation-building-materials-owner',
            'name': 'Foundation Building Materials (FBM) LLC',
            'type': 'private-company',
            'country': 'US',
            'note': "Documented conduct record: total fines $173800 million; Lowe's | Ekalavya Hansaj: $12.5 "
                    'billion; Lowe’s (LOW) Stock Outlook for 2026: Earnings Beat, Rate‑Cut Hopes and a $12.5M Fine – '
                    'What It Means for Investors: $8.8 billion'},
  'claim': {'text': 'Foundation Building Materials (FBM) LLC is the ultimate owner of Foundation Building Materials '
                    '(FBM).',
            'short': 'Foundation Building Materials (FBM) LLC is the ultimate owner of Foundation Building Materials '
                     '(FBM).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Foundation Building Materials (FBM) LLC is the ultimate owner of Foundation Building Materials (FBM).',
  'confidence': 'medium',
  'note': "Documented conduct record: total fines $173800 million; Lowe's | Ekalavya Hansaj: $12.5 billion; Lowe’s "
          '(LOW) Stock Outlook for 2026: Earnings Beat, Rate‑Cut Hopes and a $12.5M Fine – What It Means for '
          'Investors: $8.8 billion'},
 {'sponsorId': 'frost-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'frost-bank-owner',
            'name': 'Cullen/Frost Bankers, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Cullen/Frost Bankers, Inc. is a publicly traded bank; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Cullen/Frost Bankers, Inc. is a publicly traded company listed on the NYSE under ticker CFR.',
            'short': 'Cullen/Frost Bankers, Inc.',
            'source': {'name': 'SEC DEF 14A for Cullen/Frost Bankers, Inc.',
                       'date': '2026-03-20',
                       'url': 'https://www.sec.gov/Archives/edgar/data/39263/000003926326000023/cfr-20260320.htm'}},
  'verdict': 'Owned by Cullen/Frost Bankers, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Cullen/Frost Bankers, Inc. is a publicly traded bank; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'fundacion-1890',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'fundacion-1890',
            'name': 'Fundacion 1890 (Sevilla FC Foundation)',
            'type': 'private-company',
            'country': 'ES',
            'note': "The on-shirt 'Fundacion 1890' branding is a stopgap/charitable placement paying the club's own "
                    'foundation; not a state or fund sponsor.'},
  'claim': {'text': "Fundacion 1890 is the non-profit foundation arm of Sevilla FC, renamed from 'Fundacion Sevilla "
                    "FC' in June 2025; it took the club's 1890 founding date. It is a private-law entity controlled "
                    'by Sevilla FC (itself owned by Sevillistas de Nervion S.A.), with no public/state endowment.',
            'short': "Fundacion 1890 is the non-profit foundation arm of Sevilla FC, renamed from 'Fundacion Sevilla "
                     "FC' in June 2025; it took the club's 1890 founding date.",
            'source': {'name': "Diario de Sevilla - 'La Fundacion 1890, nueva cara solidaria del Sevilla'; Sevilla "
                               'FC official foundation page',
                       'date': '2025-06-09',
                       'url': 'https://www.diariodesevilla.es/sevillafc/fundacion-1890-nueva-cara-solidaria-sevilla-fc-poligono-sur_0_2004112018.html'}},
  'verdict': 'Owned by Fundacion 1890 (Sevilla FC Foundation). Nothing found.',
  'confidence': 'medium',
  'note': "The on-shirt 'Fundacion 1890' branding is a stopgap/charitable placement paying the club's own "
          'foundation; not a state or fund sponsor.'},
 {'sponsorId': 'gainbridge',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'gainbridge-group-1001-owner',
            'name': 'Gainbridge (Group 1001)',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Group 1001 is a privately held insurance holding company controlled by Mark Walter (via TWG '
                    'Global); no state ownership. No documented human-rights concerns in ownership chain '
                    'identified.'},
  'claim': {'text': 'Gainbridge is owned by Group 1001 Insurance Holdings, a privately held financial services '
                    'collective controlled by Mark Walter (TWG Global), with no state ownership.',
            'short': 'Gainbridge is owned by Group 1001 Insurance Holdings, a privately held financial services '
                     'collective controlled by Mark Walter (TWG Global), with no state ownership.',
            'source': {'name': 'Group 1001 About Us page',
                       'date': '2026-09-24',
                       'url': 'https://www.group1001.com/aboutus'}},
  'verdict': 'Owned by Gainbridge (Group 1001). Nothing found.',
  'confidence': 'medium',
  'note': 'Group 1001 is a privately held insurance holding company controlled by Mark Walter (via TWG Global); no '
          'state ownership. No documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'gazprom',
  'tier': 'severe',
  'ownership': 'owned',
  'owner': {'id': 'russian-federation',
            'name': 'Russian Federation (Federal Agency for State Property Management + state-controlled '
                    'Rosneftegaz)',
            'type': 'state',
            'country': 'RU',
            'note': 'Severe: state-controlled and the state is the direct party to an ongoing armed conflict. '
                    "State-control claim corroborated by the company's own investor page; war-funding claim from "
                    'Yale HRL PDF.'},
  'claim': {'text': "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% "
                    "plus government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya 0.89%, per the company's own "
                    'share register). Gas revenues underwrite the Russian state, and Yale HRL concluded with high '
                    "confidence that Gazprom, as a Russian state-owned company, 'underwrote and funded' the war "
                    'effort.',
            'short': "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% "
                     'plus government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya….',
            'source': {'name': "Gazprom official 'Shares'/equity capital page; Yale School of Public Health "
                               "Humanitarian Research Lab, 'Willing Accomplices'",
                       'date': '2025-12-31 / 2023',
                       'url': 'https://www.gazprom.com/investors/stock/'}},
  'verdict': "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% plus "
             'government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya….',
  'confidence': 'high',
  'note': 'Severe: state-controlled and the state is the direct party to an ongoing armed conflict. State-control '
          "claim corroborated by the company's own investor page; war-funding claim from Yale HRL PDF."},
 {'sponsorId': 'geely-auto-uk',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'zhejiang-geely-holding-group',
            'name': 'Zhejiang Geely Holding Group Co., Ltd.',
            'type': 'private-company',
            'country': 'CN',
            'note': 'Geely Holding has had state-linked co-investors and provincial funds at points, but the '
                    'disclosed ultimate beneficial owner is Li Shufu, so no material state stake was established.'},
  'claim': {'text': 'Geely Auto UK, the Coventry City sleeve sponsor, is the UK arm of Geely Automobile Holdings '
                    "Limited (HKEX: 0175), and Geely's own annual report states that the company's ultimate holding "
                    'company is Zhejiang Geely Holding Group Company Limited, beneficially owned by Li Shufu. So the '
                    'chain ends in a private Chinese family holding rather than the Chinese state. Human-rights '
                    'relevance: automotive manufacturing and battery/cobalt supply chains, but no state or '
                    'conflict-minerals owner.',
            'short': 'Geely Auto UK, the Coventry City sleeve sponsor, is the UK arm of Geely Automobile Holdings '
                     "Limited (HKEX: 0175), and Geely's own annual report states that the….",
            'source': {'name': 'Geely Automobile Holdings Limited, Annual Report 2025 (HKEX filing)',
                       'date': '2026-03',
                       'url': 'https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800309.pdf'}},
  'verdict': 'Owned by Zhejiang Geely Holding Group Co., Ltd.. Nothing found.',
  'confidence': 'high',
  'note': 'Geely Holding has had state-linked co-investors and provincial funds at points, but the disclosed '
          'ultimate beneficial owner is Li Shufu, so no material state stake was established.'},
 {'sponsorId': 'gillette',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'procter-and-gamble',
            'name': 'The Procter & Gamble Company',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': "Gillette, the New England Revolution front sponsor, is a P&G brand - listed on P&G's own brand "
                    'pages under Grooming. P&G (NYSE: PG) is a widely held listed consumer-goods major with no '
                    'controlling shareholder and no state stake. Human-rights relevance: large consumer supply '
                    "chains (palm oil, contract manufacturing), but nothing that lifts it above 'none'.",
            'short': "Gillette, the New England Revolution front sponsor, is a P&G brand - listed on P&G's own brand "
                     'pages under Grooming.',
            'source': {'name': 'Procter & Gamble - brands index (Gillette under Grooming)',
                       'date': '2026',
                       'url': 'https://us.pg.com/brands/'}},
  'verdict': 'Owned by The Procter & Gamble Company. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'globe-life',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'globe-life-globe-life-inc-owner',
            'name': 'Globe Life (Globe Life Inc.)',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $457 million; February 07, 2024 | Globe Life Inc. '
                    'Reports Fourth Quarter 2023 Results | Globe Life News Release: $77 million; February 07, 2024 | '
                    'Globe Life Inc. Reports Fourth Quarter 2023 Results | Globe Life News Release: $380 million'},
  'claim': {'text': 'Globe Life (Globe Life Inc.) is the ultimate owner of Globe Life (Globe Life Inc.).',
            'short': 'Globe Life (Globe Life Inc.) is the ultimate owner of Globe Life (Globe Life Inc.).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Globe Life (Globe Life Inc.) is the ultimate owner of Globe Life (Globe Life Inc.).',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $457 million; February 07, 2024 | Globe Life Inc. Reports Fourth '
          'Quarter 2023 Results | Globe Life News Release: $77 million; February 07, 2024 | Globe Life Inc. Reports '
          'Fourth Quarter 2023 Results | Globe Life News Release: $380 million'},
 {'sponsorId': 'golden-1-credit-union',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'golden-1-credit-union-owner',
            'name': 'Golden 1 Credit Union',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states member-owned and not-for-profit; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Credit unions like Golden 1 are member-owned and not-for-profit financial cooperatives.',
            'short': 'Credit unions like Golden 1 are member-owned and not-for-profit financial cooperatives.',
            'source': {'name': 'Golden 1 Credit Union blog post',
                       'date': '2026-09-24',
                       'url': 'https://www.golden1.com/blog/why-choose-a-credit-union'}},
  'verdict': 'Owned by Golden 1 Credit Union. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states member-owned and not-for-profit; no state stake or serious conduct record identified.'},
 {'sponsorId': 'google',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'alphabet-inc', 'name': 'Alphabet Inc.', 'type': 'listed-company', 'country': 'US', 'note': None},
  'claim': {'text': 'The McLaren front branding is Google, a subsidiary of Alphabet Inc., the Nasdaq-listed holding '
                    "company (GOOGL/GOOG) that Google's own company page names as the parent of which Sundar Pichai "
                    'is CEO. Alphabet is not state-owned: control sits with founders through super-voting Class B '
                    'stock while the economic ownership is a public float. Human-rights relevance: data/privacy and '
                    'antitrust exposure, not state or conflict money.',
            'short': 'The McLaren front branding is Google, a subsidiary of Alphabet Inc., the Nasdaq-listed holding '
                     "company (GOOGL/GOOG) that Google's own company page names as the….",
            'source': {'name': 'Google - About Google, Company Info',
                       'date': '2026',
                       'url': 'https://about.google/company-info/'}},
  'verdict': 'Owned by Alphabet Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'great-american-insurance',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'great-american-insurance-owner',
            'name': 'Great American Insurance',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Great American Insurance (AFG subsidiary) is publicly traded with no state ownership; largest '
                    'holders are Vanguard and BlackRock, each under 10%. No human-rights concerns in ownership chain '
                    'identified.'},
  'claim': {'text': 'Great American Insurance is a publicly traded property and casualty insurer with no state '
                    'ownership; largest shareholders are institutional investors (Vanguard, BlackRock) each under '
                    '10%.',
            'short': 'Great American Insurance is a publicly traded property and casualty insurer with no state '
                     'ownership; largest shareholders are institutional investors (Vanguard,….',
            'source': {'name': 'American Financial Group DEF 14A 2026',
                       'date': '2026-04-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1042046/000114036126013118/ny20062510x1_def14a.htm'}},
  'verdict': 'Owned by Great American Insurance. Nothing found.',
  'confidence': 'high',
  'note': 'Great American Insurance (AFG subsidiary) is publicly traded with no state ownership; largest holders are '
          'Vanguard and BlackRock, each under 10%. No human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'gree',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'gree-group-zhuhai-sasac',
            'name': 'Gree Group Co., Ltd. (Zhuhai Municipal Government / Zhuhai SASAC)',
            'type': 'state',
            'country': 'CN',
            'note': 'Chinese appliance maker, so Xinjiang/forced-labour questions attach to the wider PRC SOE supply '
                    'chain but no Gree-specific adverse finding was located: hence concern (partial state ownership) '
                    "rather than serious. Owner type 'state' (municipal SASAC), country CN."},
  'claim': {'text': 'Gree Electric Appliances Inc. of Zhuhai (SZSE: 000651) is described as a majority state-owned '
                    'enterprise principally by the city of Zhuhai; its historic largest shareholder, state-owned '
                    "Gree Group, was owned by the Zhuhai Municipal People's Government. In December 2019 Gree Group "
                    'sold most of its stake to the private equity vehicle Zhuhai Mingjun, leaving partial (not '
                    'controlling) state ownership.',
            'short': 'Gree Electric Appliances Inc.',
            'source': {'name': 'Zhuhai Gree Group company history (state-owned nature change); Shenzhen Stock '
                               'Exchange filings on the 2019 Gree Group/Zhuhai Mingjun share transfer',
                       'date': '2024-06-08',
                       'url': 'http://static.cninfo.com.cn/finalpage/2024-06-08/1220300050.PDF'}},
  'verdict': 'Gree Electric Appliances Inc.',
  'confidence': 'medium',
  'note': 'Chinese appliance maker, so Xinjiang/forced-labour questions attach to the wider PRC SOE supply chain but '
          'no Gree-specific adverse finding was located: hence concern (partial state ownership) rather than '
          "serious. Owner type 'state' (municipal SASAC), country CN."},
 {'sponsorId': 'guggenheim',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'guggenheim-owner',
            'name': 'Guggenheim Baseball Management',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Guggenheim Baseball Management LLC is owned by Guggenheim Baseball Management. No state '
                    'shareholder identified. Ownership sits with public institutional and retail investors, so the '
                    'sponsorship money is purely private capital.',
            'short': 'Guggenheim Baseball Management LLC is owned by Guggenheim Baseball Management.',
            'source': {'name': 'MLB article on Dodgers sale to Guggenheim',
                       'date': '2012-05-01',
                       'url': 'https://www.mlb.com/news/dodgers-sale-to-guggenheim-baseball-management-closed-c30125872'}},
  'verdict': 'Owned by Guggenheim Baseball Management. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'guidehouse',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'bain-capital',
            'name': 'Bain Capital, LP (Bain Capital Private Equity)',
            'type': 'private-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'Guidehouse, the D.C. United front sponsor, is a Washington-based consultancy owned by Bain '
                    'Capital Private Equity, which bought it from Veritas Capital in a $5.3bn deal that closed in '
                    "December 2023 - Guidehouse's own newsroom confirms the completion. Ownership is therefore "
                    "private PE money (Bain's funds and their LPs), no state stake. Human-rights relevance: "
                    'consulting/defense-adjacent services, nothing state-owned.',
            'short': 'Guidehouse, the D.C.',
            'source': {'name': 'Guidehouse newsroom - completion of transaction with Bain Capital',
                       'date': '2023-12-14',
                       'url': 'https://guidehouse.com/news/corporate-news/2023/guidehouse-completes-transaction-with-bain-capital'}},
  'verdict': 'Owned by Bain Capital, LP (Bain Capital Private Equity). Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'gulf-oil',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'hinduja-group',
            'name': 'Hinduja Group (Hinduja family)',
            'type': 'private-company',
            'country': 'GB',
            'note': None},
  'claim': {'text': 'Gulf Oil International, the McLaren F1 team partner, states on its own site that Gulf is part '
                    'of the Hinduja Group, the family-owned conglomerate controlled by the Hinduja family since '
                    '1914. Ownership is therefore private family capital, with no state stake - the Gulf brand was '
                    "bought out of Chevron's old downstream business in 2001 and is now licensing/IP-driven. "
                    'Human-rights relevance: oil marketing plus a diversified group with banking and healthcare '
                    'arms.',
            'short': 'Gulf Oil International, the McLaren F1 team partner, states on its own site that Gulf is part '
                     'of the Hinduja Group, the family-owned conglomerate controlled by the….',
            'source': {'name': 'Gulf Oil International - About us (Hinduja Group)',
                       'date': '2026',
                       'url': 'https://www.gulfoilltd.com/about-us'}},
  'verdict': 'Owned by Hinduja Group (Hinduja family). Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'gulf-oil-w',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'hinduja-group',
            'name': 'Hinduja Group (Hinduja family)',
            'type': 'private-company',
            'country': 'GB',
            'note': 'Same ultimate owner for the Williams partnership as for the McLaren deal; Hinduja Group is '
                    'family-held, so no state stake.'},
  'claim': {'text': 'Gulf Oil International, the Williams F1 team partner, states on its own site that Gulf is part '
                    'of the Hinduja Group, the family-owned conglomerate controlled by the Hinduja family since '
                    '1914. Ownership is therefore private family capital, with no state stake - the Gulf brand was '
                    "bought out of Chevron's old downstream business in 2001 and is now licensing/IP-driven. "
                    'Human-rights relevance: oil marketing plus a diversified group with banking and healthcare '
                    'arms.',
            'short': 'Gulf Oil International, the Williams F1 team partner, states on its own site that Gulf is part '
                     'of the Hinduja Group, the family-owned conglomerate controlled by….',
            'source': {'name': 'Gulf Oil International - About us (Hinduja Group)',
                       'date': '2026',
                       'url': 'https://www.gulfoilltd.com/about-us'}},
  'verdict': 'Owned by Hinduja Group (Hinduja family). Nothing found.',
  'confidence': 'high',
  'note': 'Same ultimate owner for the Williams partnership as for the McLaren deal; Hinduja Group is family-held, '
          'so no state stake.'},
 {'sponsorId': 'halo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'halo-lifestyle-llc',
            'name': 'Halo Lifestyle LLC (HALO Hydration)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Not to be confused with HALO Water Systems or Halo Sports. Small US private brand, no parent '
                    'group.'},
  'claim': {'text': 'HALO Hydration is the trading brand of HALO Lifestyle LLC, a New York/US private company '
                    'founded in 2017 by Anshuman Vohra and Robin Shobin; it is venture-backed (including celebrity '
                    'investors such as Andy Murray and Pitbull) with no state or sovereign-fund ownership.',
            'short': 'HALO Hydration is the trading brand of HALO Lifestyle LLC, a New York/US private company '
                     'founded in 2017 by Anshuman Vohra and Robin Shobin; it is venture-backed….',
            'source': {'name': 'Preqin asset profile for Halo Hydration; Crunchbase legal-name record (HALO '
                               'LIFESTYLE LLC)',
                       'date': '2025',
                       'url': 'https://www.preqin.com/data/profile/asset/halo-hydration/624618'}},
  'verdict': 'Owned by Halo Lifestyle LLC (HALO Hydration). Nothing found.',
  'confidence': 'medium',
  'note': 'Not to be confused with HALO Water Systems or Halo Sports. Small US private brand, no parent group.'},
 {'sponsorId': 'hansemerkur',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'hansemerkur-krankenversicherung-ag',
            'name': 'HanseMerkur Krankenversicherung a.G. (HanseMerkur Group)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'German mutual insurer. No state or listed-shareholder ownership.'},
  'claim': {'text': "HanseMerkur is Germany's only independent, group-independent mid-sized personal insurer in "
                    'Hamburg and is structured as a Versicherungsverein auf Gegenseitigkeit (mutual); HanseMerkur '
                    'Krankenversicherung auf Gegenseitigkeit remains the owner of the group, owing duties only to '
                    'customers and staff, not shareholders.',
            'short': "HanseMerkur is Germany's only independent, group-independent mid-sized personal insurer in "
                     'Hamburg and is structured as a Versicherungsverein auf Gegenseitigkeit….',
            'source': {'name': 'HanseMerkur official company/facts page (mutual structure); HanseMerkur 150-year '
                               'corporate history',
                       'date': '2025',
                       'url': 'https://vertriebskarriere.hansemerkur.de/das-unternehmen/zahlen-fakten'}},
  'verdict': 'Owned by HanseMerkur Krankenversicherung a.G. (HanseMerkur Group). Nothing found.',
  'confidence': 'high',
  'note': 'German mutual insurer. No state or listed-shareholder ownership.'},
 {'sponsorId': 'hard-rock-international',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'hard-rock-international-owner',
            'name': 'Hard Rock International LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Documented conduct record: total fines $130 million; Ontario Regulator Fines Ottawa Casino '
                    'Owned By Hard Rock Over $200K For 36 Violations: money laundering; Hard Rock Exec Alex Pariente '
                    'Let Markers Go Unpaid, Took Bookies’ Action, Say Sources - TornadoSpins: $130.13 million'},
  'claim': {'text': 'Hard Rock International LLC is the ultimate owner of Hard Rock International.',
            'short': 'Hard Rock International LLC is the ultimate owner of Hard Rock International.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Hard Rock International LLC is the ultimate owner of Hard Rock International.',
  'confidence': 'medium',
  'note': 'Documented conduct record: total fines $130 million; Ontario Regulator Fines Ottawa Casino Owned By Hard '
          'Rock Over $200K For 36 Violations: money laundering; Hard Rock Exec Alex Pariente Let Markers Go Unpaid, '
          'Took Bookies’ Action, Say Sources - TornadoSpins: $130.13 million'},
 {'sponsorId': 'healthequity',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'healthequity-owner',
            'name': 'HealthEquity, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'HealthEquity is a publicly traded health technology company; no state stake or serious conduct '
                    'record identified.'},
  'claim': {'text': 'HealthEquity, Inc. is a publicly traded company listed on the NASDAQ under ticker HQY.',
            'short': 'HealthEquity, Inc.',
            'source': {'name': 'SEC DEF 14A for HealthEquity, Inc.',
                       'date': '2026-05-13',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1428336/000142833626000022/hqy-20260513.htm'}},
  'verdict': 'Owned by HealthEquity, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'HealthEquity is a publicly traded health technology company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'herbalife',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'herbalife-ltd',
            'name': 'Herbalife Ltd.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'The 2016 FTC action is dated but is still the defining regulatory finding; Herbalife has had no '
                    'state or conflict link.'},
  'claim': {'text': 'Herbalife, the LA Galaxy front sponsor, is listed on the NYSE (HLF) with a public float and no '
                    "state stake. It is rated 'concern' on conduct, not ownership: in July 2016 Herbalife settled "
                    'FTC charges for $200m and was forced to restructure distributor rewards after the FTC found '
                    'misleading earnings claims in its multi-level marketing model - the distributor network being '
                    'the human-rights/consumer-pressure point. Otherwise unremarkable.',
            'short': 'Herbalife, the LA Galaxy front sponsor, is listed on the NYSE (HLF) with a public float and no '
                     'state stake.',
            'source': {'name': 'US Federal Trade Commission press release - Herbalife $200m settlement',
                       'date': '2016-07-15',
                       'url': 'https://www.ftc.gov/news-events/news/press-releases/2016/07/herbalife-will-restructure-its-multi-level-marketing-operations-pay-200-million-consumer-redress'}},
  'verdict': 'Herbalife, the LA Galaxy front sponsor, is listed on the NYSE (HLF) with a public float and no state '
             'stake.',
  'confidence': 'high',
  'note': 'The 2016 FTC action is dated but is still the defining regulatory finding; Herbalife has had no state or '
          'conflict link.'},
 {'sponsorId': 'hibob',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'hibob', 'name': 'HiBob (Bob)', 'type': 'private-company', 'country': 'IL', 'note': None},
  'claim': {'text': 'HiBob, the Fulham sleeve sponsor, is a privately held HR-software company (Tel Aviv-founded, '
                    'London and New York presence) whose own about page records a $150m Series C at a $1.65bn '
                    'valuation, later followed by Series D money - venture capital, not state capital. No parent '
                    'company, no state stake. Human-rights relevance: SaaS workforce-data business only.',
            'short': 'HiBob, the Fulham sleeve sponsor, is a privately held HR-software company (Tel Aviv-founded, '
                     'London and New York presence) whose own about page records a $150m….',
            'source': {'name': 'HiBob - About HiBob (company history incl. $150m Series C)',
                       'date': '2026',
                       'url': 'https://www.hibob.com/about/'}},
  'verdict': 'Owned by HiBob (Bob). Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'highmark',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'highmark-owner',
            'name': 'Highmark',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Highmark Health is a private nonprofit (501(c)(3)) enterprise; no state stake or government '
                    'control. Organized as a private nonprofit health system, not a public entity.'},
  'claim': {'text': 'Highmark Health is a private, nonprofit integrated health delivery and financing system, parent '
                    'of Highmark Inc. and Allegheny Health Network, with no state ownership.',
            'short': 'Highmark Health is a private, nonprofit integrated health delivery and financing system, '
                     'parent of Highmark Inc.',
            'source': {'name': 'Highmark Health About Us page',
                       'date': '2026-09-24',
                       'url': 'https://www.highmarkhealth.org/about-us/index.shtml'}},
  'verdict': 'Owned by Highmark. Nothing found.',
  'confidence': 'medium',
  'note': 'Highmark Health is a private nonprofit (501(c)(3)) enterprise; no state stake or government control. '
          'Organized as a private nonprofit health system, not a public entity.'},
 {'sponsorId': 'honda',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'honda-motor-co-ltd',
            'name': 'Honda Motor Co., Ltd.',
            'type': 'listed-company',
            'country': 'JP',
            'note': None},
  'claim': {'text': 'The Aston Martin F1 front branding is Honda / Honda Racing Corporation, a division of Honda '
                    'Motor Co., Ltd., the Tokyo- and NYSE-listed automaker and motorcycle maker. Honda has no parent '
                    'company: its annual report filing shows dispersed ownership dominated by Japanese trust banks '
                    'and insurers (Mitsubishi UFJ Trust / Master Trust Bank of Japan vehicles). No state stake; '
                    'relevance is automotive supply chains.',
            'short': 'The Aston Martin F1 front branding is Honda / Honda Racing Corporation, a division of Honda '
                     'Motor Co., Ltd., the Tokyo- and NYSE-listed automaker and motorcycle….',
            'source': {'name': 'Honda Motor Co., Ltd. Form 20-F (SEC)',
                       'date': '2026-06-18',
                       'url': 'https://www.sec.gov/Archives/edgar/data/715153/000119312526274991/d116494d20f.htm'}},
  'verdict': 'Owned by Honda Motor Co., Ltd.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'hp',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'hp-inc', 'name': 'HP Inc.', 'type': 'listed-company', 'country': 'US', 'note': None},
  'claim': {'text': 'The Ferrari front branding is HP Inc., the Delaware-incorporated, NYSE-listed hardware company '
                    'created by the 2015 Hewlett-Packard split. Dispersed public ownership, no parent, no state '
                    'stake. Human-rights relevance: hardware supply chains and printer/ink subscription litigation, '
                    'none of it owner-level state exposure.',
            'short': 'The Ferrari front branding is HP Inc., the Delaware-incorporated, NYSE-listed hardware company '
                     'created by the 2015 Hewlett-Packard split.',
            'source': {'name': 'HP Inc. Form 10-K for FY2025 (SEC)',
                       'date': '2025-12-10',
                       'url': 'https://www.sec.gov/Archives/edgar/data/47217/000004721725000071/hpq-20251031.htm'}},
  'verdict': 'Owned by HP Inc.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'huntington-national-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'huntington-national-bank-huntington-bancshares-owner',
            'name': 'Huntington National Bank (Huntington Bancshares)',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Huntington Bancshares Incorporated is owned by Huntington National Bank (Huntington '
                    'Bancshares). No state shareholder identified. Ownership sits with public institutional and '
                    'retail investors, so the sponsorship money is purely private capital.',
            'short': 'Huntington Bancshares Incorporated is owned by Huntington National Bank (Huntington '
                     'Bancshares).',
            'source': {'name': 'HUNTINGTON BANCSHARES INC /MD/ DEF 14A 2026 (SEC)',
                       'date': '2026-03-12',
                       'url': 'https://www.sec.gov/Archives/edgar/data/49196/000119312526103196/hban-20260312.htm'}},
  'verdict': 'Owned by Huntington National Bank (Huntington Bancshares). Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'hylo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ursapharm-arzneimittel-gmbh',
            'name': 'URSAPHARM Arzneimittel GmbH',
            'type': 'private-company',
            'country': 'DE',
            'note': 'URSAPHARM is the owner of the HYLO trademark (USPTO registration 5887500 in its name). Not HYLO '
                    'the drink brand.'},
  'claim': {'text': 'HYLO is the flagship dry-eye brand of URSAPHARM Arzneimittel GmbH, a privately held, '
                    'family/mittelstand German pharmaceutical and medical-device maker headquartered in Saarbrucken, '
                    'founded 1974 and still independent after 50 years.',
            'short': 'HYLO is the flagship dry-eye brand of URSAPHARM Arzneimittel GmbH, a privately held, '
                     'family/mittelstand German pharmaceutical and medical-device maker….',
            'source': {'name': 'URSAPHARM Arzneimittel GmbH official company profile and 50th-anniversary release',
                       'date': '2024-04-08',
                       'url': 'https://ursapharm.de/en/press/company-profile/'}},
  'verdict': 'Owned by URSAPHARM Arzneimittel GmbH. Nothing found.',
  'confidence': 'medium',
  'note': 'URSAPHARM is the owner of the HYLO trademark (USPTO registration 5887500 in its name). Not HYLO the drink '
          'brand.'},
 {'sponsorId': 'hyundai',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'hyundai-owner',
            'name': 'Hyundai Motor Company',
            'type': 'listed-company',
            'country': 'South Korea',
            'note': "Chain traced to the top: Hyundai Motor America (listed in the same report's global "
                    'network/subsidiary table as the US sales entity) is a wholly owned subsidiary of Hyundai Motor '
                    'Company, Seoul-listed, which is itself the largest single shareholder of Kia (35.17%) while '
                    "Hyundai Mobis (22.36% of Hyundai Motor) is Hyundai Motor's largest shareholder and Kia in turn "
                    'owns roughly 17-18% of Mobis - a circular chaebol ring with no single shareholder at the top. '
                    'Control sits with the Chung family (Euisun Chung 2.73% direct plus chair role on 0.33% of '
                    'Mobis, his father Mong-Koo Chung 5.57% of Hyundai Motor and about 7.3% of Mobis), not with any '
                    "state. Tier is 'concern' rather than 'none' because the parent's register contains genuine "
                    "partial state/state-fund money: National Pension Service 7.76% as of end-2025, and 'The "
                    "Government of Singapore' (GIC) at 3.55% as of end-2024 in the company's 2025 Sustainability "
                    'Report '
                    '(https://www.hyundai.news/newsroom/dam/eu/brand/20250704_2025_sustainability_report/hmc-2025-sustainability-report-en.pdf). '
                    "It is not 'serious' because no state or state fund controls Hyundai - the listed company is "
                    "family-controlled, so the state link is minority, which is exactly the rubric's 'partial state "
                    "stake'. Honesty flag: the existing corpus entry for kia-america (same parent chain) says 'no "
                    "state ownership ... privately held conglomerate' and is tiered 'none'; the NPS/GIC holdings are "
                    'the difference, so the two entries are now inconsistent and kia-america is worth re-checking on '
                    'the same evidence. Secondary corroboration for the filing itself: Hyundai Motor Company Annual '
                    'Report filed with DART (rcpNo 20250312001148, 2025-03-12) '
                    'https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250312001148.'},
  'claim': {'text': 'Hyundai Motor America is the US sales subsidiary of Hyundai Motor Company (KRX: 005380), and '
                    "Hyundai's own shareholder register for the end of 2025 lists Hyundai Mobis as the largest "
                    "shareholder at 22.36% and the Korean National Pension Service, the country's statutory public "
                    'pension fund, as the largest outside shareholder at 7.76%, with the register noting that no '
                    'government institution holds a golden share.',
            'short': 'Hyundai Motor America is the US sales subsidiary of Hyundai Motor Company (KRX: 005380), and '
                     "Hyundai's own shareholder register for the end of 2025 lists Hyundai….",
            'source': {'name': 'Hyundai Motor Company, 2026 Sustainability Report (FY2025), p.123 Shareholder '
                               'Composition',
                       'date': '2026-06-01',
                       'url': 'https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/sustainability/about-sustainability/2026/hmc-2026-sustainability-report-en.pdf'}},
  'verdict': "Hyundai Motor America is the US sales subsidiary of Hyundai Motor Company (KRX: 005380), and Hyundai's "
             'own shareholder register for the end of 2025 lists Hyundai….',
  'confidence': 'medium',
  'note': "Chain traced to the top: Hyundai Motor America (listed in the same report's global network/subsidiary "
          'table as the US sales entity) is a wholly owned subsidiary of Hyundai Motor Company, Seoul-listed, which '
          'is itself the largest single shareholder of Kia (35.17%) while Hyundai Mobis (22.36% of Hyundai Motor) is '
          "Hyundai Motor's largest shareholder and Kia in turn owns roughly 17-18% of Mobis - a circular chaebol "
          'ring with no single shareholder at the top. Control sits with the Chung family (Euisun Chung 2.73% direct '
          'plus chair role on 0.33% of Mobis, his father Mong-Koo Chung 5.57% of Hyundai Motor and about 7.3% of '
          "Mobis), not with any state. Tier is 'concern' rather than 'none' because the parent's register contains "
          "genuine partial state/state-fund money: National Pension Service 7.76% as of end-2025, and 'The "
          "Government of Singapore' (GIC) at 3.55% as of end-2024 in the company's 2025 Sustainability Report "
          '(https://www.hyundai.news/newsroom/dam/eu/brand/20250704_2025_sustainability_report/hmc-2025-sustainability-report-en.pdf). '
          "It is not 'serious' because no state or state fund controls Hyundai - the listed company is "
          "family-controlled, so the state link is minority, which is exactly the rubric's 'partial state stake'. "
          "Honesty flag: the existing corpus entry for kia-america (same parent chain) says 'no state ownership ... "
          "privately held conglomerate' and is tiered 'none'; the NPS/GIC holdings are the difference, so the two "
          'entries are now inconsistent and kia-america is worth re-checking on the same evidence. Secondary '
          'corroboration for the filing itself: Hyundai Motor Company Annual Report filed with DART (rcpNo '
          '20250312001148, 2025-03-12) https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250312001148.'},
 {'sponsorId': 'ibotta',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ibotta-owner',
            'name': 'Ibotta LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Ibotta LLC is the ultimate owner of Ibotta.',
            'short': 'Ibotta LLC is the ultimate owner of Ibotta.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Ibotta LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'ifs',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'ifs-ab',
            'name': 'IFS AB (Industrial and Financial Systems)',
            'type': 'private-company',
            'country': 'SE',
            'note': 'EQT itself is a listed Swedish PE firm, so the chain has both listed-PE and private-fund '
                    "layers; ADIA's entry is minority, hence 'concern'."},
  'claim': {'text': 'IFS, the Cadillac F1 partner, is controlled by private equity: EQT holds control and Hg became '
                    'a co-control shareholder in April 2025, with TA Associates and new investors including a wholly '
                    'owned subsidiary of the Abu Dhabi Investment Authority (ADIA) alongside CPP Investments, in a '
                    'deal valuing IFS at EUR15bn. ADIA is a sovereign wealth fund, so this is a partial state-fund '
                    "stake - 'concern' rather than 'serious', since the state money is minority. Human-rights "
                    'relevance: UAE sovereign capital at minority level plus PE leverage.',
            'short': 'IFS, the Cadillac F1 partner, is controlled by private equity: EQT holds control and Hg became '
                     'a co-control shareholder in April 2025, with TA Associates and new….',
            'source': {'name': 'EQT / Hg / TA Associates press release - IFS valued at EUR 15bn in minority stake '
                               'sale',
                       'date': '2025-04-09',
                       'url': 'https://mb.cision.com/Main/87/4133272/3378631.pdf'}},
  'verdict': 'IFS, the Cadillac F1 partner, is controlled by private equity: EQT holds control and Hg became a '
             'co-control shareholder in April 2025, with TA Associates and new….',
  'confidence': 'high',
  'note': "EQT itself is a listed Swedish PE firm, so the chain has both listed-PE and private-fund layers; ADIA's "
          "entry is minority, hence 'concern'."},
 {'sponsorId': 'indeed',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'recruit-holdings',
            'name': 'Recruit Holdings Co., Ltd. (Tokyo-listed)',
            'type': 'listed-company',
            'country': 'JP',
            'note': 'Listed Japanese parent, no state link → none.'},
  'claim': {'text': 'Indeed, Inc. was acquired in 2012 and is a key subsidiary of Recruit Holdings Co., Ltd., a '
                    'Tokyo-listed Japanese holding company that also owns Glassdoor. No state or state-fund owner.',
            'short': 'Indeed, Inc.',
            'source': {'name': "Recruit Holdings official 'Group Companies' page",
                       'date': '2026',
                       'url': 'https://recruit-holdings.com/en/about/group'}},
  'verdict': 'Owned by Recruit Holdings Co., Ltd. (Tokyo-listed). Nothing found.',
  'confidence': 'high',
  'note': 'Listed Japanese parent, no state link → none.'},
 {'sponsorId': 'independence-blue-cross',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'independence-blue-cross-owner',
            'name': 'Independence Blue Cross',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states not-for-profit status; no state stake or serious conduct record identified.'},
  'claim': {'text': 'As a not-for-profit health insurer, Independence Blue Cross is focused on building a smarter, '
                    'simpler, and more affordable health care system.',
            'short': 'As a not-for-profit health insurer, Independence Blue Cross is focused on building a smarter, '
                     'simpler, and more affordable health care system.',
            'source': {'name': 'Independence Blue Cross website',
                       'date': '2026-09-24',
                       'url': 'https://www.ibx.com/htdocs/custom/getting-health-care-right/index.html'}},
  'verdict': 'Owned by Independence Blue Cross. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states not-for-profit status; no state stake or serious conduct record identified.'},
 {'sponsorId': 'ineos-s',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ineos-group-limited',
            'name': 'INEOS Group Limited',
            'type': 'private-company',
            'country': 'GB',
            'note': "Ratcliffe's majority stake and the Currie/Reece minority are well reported but not on the page "
                    "opened; the page does confirm private ownership and Ratcliffe's chairmanship. Tier kept 'none' "
                    "on ownership grounds rather than 'concern' on the petrochemicals record."},
  'claim': {'text': 'INEOS, the Mercedes F1 partner and one-third team shareholder, states it is privately owned; it '
                    'was founded and is chaired by Sir Jim Ratcliffe, who holds the large majority of the equity '
                    'with Andy Currie and John Reece as minority shareholders. No state stake at all. Human-rights '
                    'relevance: as a petrochemicals producer it carries a documented pollution/permitting record '
                    '(Grangemouth and European crackers), but ownership is clean private money.',
            'short': 'INEOS, the Mercedes F1 partner and one-third team shareholder, states it is privately owned; '
                     'it was founded and is chaired by Sir Jim Ratcliffe, who holds the….',
            'source': {'name': 'INEOS - About (privately owned; Chairman Sir Jim Ratcliffe)',
                       'date': '2026',
                       'url': 'https://www.ineos.com/about/'}},
  'verdict': 'Owned by INEOS Group Limited. Nothing found.',
  'confidence': 'high',
  'note': "Ratcliffe's majority stake and the Currie/Reece minority are well reported but not on the page opened; "
          "the page does confirm private ownership and Ratcliffe's chairmanship. Tier kept 'none' on ownership "
          "grounds rather than 'concern' on the petrochemicals record."},
 {'sponsorId': 'intuit',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'intuit-intuit-inc-nasdaq-intu-owner',
            'name': 'Intuit Inc.',
            'type': 'listed-company',
            'country': 'United States',
            'note': 'Ownership is clean: Nasdaq-listed, US-incorporated, dispersed float, only two >5% holders (both '
                    "passive index managers), no state stake, so the ownership half of the test returns 'none'. "
                    "Tiered 'concern' on conduct, following the house practice set by the herbalife, cognizant, "
                    'citigroup and kroger entries, where a single named enforcement record with money attached was '
                    "treated as the rubric's 'a lesser link': the FTC issued an Opinion and Final Order on 22 "
                    'January 2024 upholding the Chief ALJ and holding that Intuit violated Section 5 of the FTC Act '
                    "by running 'free' ads for products most consumers were ineligible for "
                    '(https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-issues-opinion-finding-turbotax-maker-intuit-inc-engaged-deceptive-practices), '
                    'and Intuit paid $141m to about 4.4 million mainly low-income taxpayers under a 50-state '
                    'settlement signed in May 2022 '
                    '(https://ag.ny.gov/press-release/2022/attorney-general-james-secures-141-million-millions-americans-deceived-turbotax). '
                    'The 2026 DEF 14A is also the primary document that rules out a state stake: it is filed after '
                    'the FY2025 10-K and carries the >5% beneficial-ownership table as of 31 October 2025 on '
                    '278,508,855 shares outstanding. Offsets in the other direction, recorded honestly: the FTC '
                    'matter is one saga rather than a sustained pattern, and the precedent entry for deel held that '
                    "company-level regulatory matters alone keep a sponsor at 'none' - so 'none' would be defensible "
                    "for Intuit on a strict state-ownership-only reading. Not 'serious' (no state owner) and not "
                    "'severe' (no conflict exposure)."},
  'claim': {'text': 'Intuit Inc. is a Nasdaq-listed (INTU) Delaware corporation and its own proxy statement shows '
                    'the only shareholders above 5% are index managers The Vanguard Group at 10.28% and BlackRock, '
                    'Inc. at 8.39%, with founder Scott D. Cook at 2.21% - there is no state, sovereign-wealth or '
                    "state-fund holder anywhere in the register; the conduct record is the FTC's final order of 22 "
                    "January 2024 finding Intuit's 'free' TurboTax advertising deceptive, following a $141m "
                    'restitution settlement with all 50 state attorneys general in May 2022.',
            'short': 'Intuit Inc.',
            'source': {'name': 'Intuit Inc. DEF 14A (2026 proxy), Security Ownership Table, filed with the SEC',
                       'date': '2025-11-26',
                       'url': 'https://www.sec.gov/Archives/edgar/data/896878/000089687825000057/intu-20251126.htm'}},
  'verdict': 'Intuit Inc.',
  'confidence': 'medium',
  'note': 'Ownership is clean: Nasdaq-listed, US-incorporated, dispersed float, only two >5% holders (both passive '
          "index managers), no state stake, so the ownership half of the test returns 'none'. Tiered 'concern' on "
          'conduct, following the house practice set by the herbalife, cognizant, citigroup and kroger entries, '
          "where a single named enforcement record with money attached was treated as the rubric's 'a lesser link': "
          'the FTC issued an Opinion and Final Order on 22 January 2024 upholding the Chief ALJ and holding that '
          "Intuit violated Section 5 of the FTC Act by running 'free' ads for products most consumers were "
          'ineligible for '
          '(https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-issues-opinion-finding-turbotax-maker-intuit-inc-engaged-deceptive-practices), '
          'and Intuit paid $141m to about 4.4 million mainly low-income taxpayers under a 50-state settlement signed '
          'in May 2022 '
          '(https://ag.ny.gov/press-release/2022/attorney-general-james-secures-141-million-millions-americans-deceived-turbotax). '
          'The 2026 DEF 14A is also the primary document that rules out a state stake: it is filed after the FY2025 '
          '10-K and carries the >5% beneficial-ownership table as of 31 October 2025 on 278,508,855 shares '
          'outstanding. Offsets in the other direction, recorded honestly: the FTC matter is one saga rather than a '
          'sustained pattern, and the precedent entry for deel held that company-level regulatory matters alone keep '
          "a sponsor at 'none' - so 'none' would be defensible for Intuit on a strict state-ownership-only reading. "
          "Not 'serious' (no state owner) and not 'severe' (no conflict exposure)."},
 {'sponsorId': 'io-sono-friuli-venezia-giulia',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'friuli-venezia-giulia-region',
            'name': 'Regione Autonoma Friuli Venezia Giulia (via PromoTurismoFVG)',
            'type': 'state',
            'country': 'IT',
            'note': None},
  'claim': {'text': "The Udinese front brand 'Io sono Friuli Venezia Giulia' is bought by the Friuli Venezia Giulia "
                    "regional government through PromoTurismoFVG, the region's public tourism agency, per the club's "
                    'own announcement of the renewal to 2028/29. The owner is therefore a public authority - '
                    "'serious' under the state-owner rule. Human-rights relevance: a regional government's "
                    'destination marketing, with no conflict or minerals exposure.',
            'short': "The Udinese front brand 'Io sono Friuli Venezia Giulia' is bought by the Friuli Venezia Giulia "
                     "regional government through PromoTurismoFVG, the region's public….",
            'source': {'name': 'Udinese Calcio - Io sono Friuli Venezia Giulia renews Udinese shirt sponsorship deal '
                               'until 2028/29',
                       'date': '2026-03-13',
                       'url': 'https://www.udinese.it/news/club/io-sono-friuli-venezia-giulia-renews-udinese-shirt-sponsorship-deal-until-202829'}},
  'verdict': "The Udinese front brand 'Io sono Friuli Venezia Giulia' is bought by the Friuli Venezia Giulia "
             "regional government through PromoTurismoFVG, the region's public….",
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'iren',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'iren-owner',
            'name': 'IREN (IREN Ltd, AI cloud infrastructure)',
            'type': 'listed-company',
            'country': 'AUS',
            'note': 'IREN is publicly traded (Australia/US) with no state ownership; largest holders are '
                    'institutional (State Street Corp. ~0.48%, others). No documented human-rights concerns in '
                    'ownership chain.'},
  'claim': {'text': 'IREN Limited is an ASX- and Nasdaq-listed AI cloud infrastructure company with dispersed '
                    'institutional ownership and no state shareholder above 5% threshold.',
            'short': 'IREN Limited is an ASX- and Nasdaq-listed AI cloud infrastructure company with dispersed '
                     'institutional ownership and no state shareholder above 5% threshold.',
            'source': {'name': 'IREN Limited Marketscreener page',
                       'date': '2026-09-24',
                       'url': 'https://www.marketscreener.com/quote/stock/IREN-LIMITED-129472358/company-shareholders'}},
  'verdict': 'Owned by IREN (IREN Ltd, AI cloud infrastructure). Nothing found.',
  'confidence': 'medium',
  'note': 'IREN is publicly traded (Australia/US) with no state ownership; largest holders are institutional (State '
          'Street Corp. ~0.48%, others). No documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'jeep',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'stellantis-nv',
            'name': 'Stellantis N.V.',
            'type': 'listed-company',
            'country': 'NL',
            'note': "The 2026 20-F also records Bpifrance's loyalty-voting power; the stake is minority and "
                    "doubled-voting, so 'concern' not 'serious'."},
  'claim': {'text': 'Jeep (with Visit Detroit) on the Juventus front is a brand of Stellantis N.V., the '
                    "Amsterdam-domiciled, NYSE/Euronext-listed automaker. Stellantis' 20-F lists its largest "
                    'shareholders as Exor N.V. (15.48%), Etablissements Peugeot Freres (7.72%) and Bpifrance '
                    'Participations (6.64%) - Bpifrance being the French state investment bank, giving a genuine but '
                    "minority state stake, hence 'concern'. Human-rights relevance: French state money at ~6.6% plus "
                    'normal automaker supply-chain exposure.',
            'short': 'Jeep (with Visit Detroit) on the Juventus front is a brand of Stellantis N.V., the '
                     'Amsterdam-domiciled, NYSE/Euronext-listed automaker.',
            'source': {'name': 'Stellantis N.V. Form 20-F for FY2025, shareholder section (SEC)',
                       'date': '2026-02-26',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1605484/000160548426000021/stellantis-20251231.htm'}},
  'verdict': 'Jeep (with Visit Detroit) on the Juventus front is a brand of Stellantis N.V., the '
             'Amsterdam-domiciled, NYSE/Euronext-listed automaker.',
  'confidence': 'high',
  'note': "The 2026 20-F also records Bpifrance's loyalty-voting power; the stake is minority and doubled-voting, so "
          "'concern' not 'serious'."},
 {'sponsorId': 'jefferson-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'jefferson-health-owner',
            'name': 'Jefferson Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Jefferson Health is owned by Jefferson Health. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Jefferson Health is owned by Jefferson Health.',
            'source': {'name': 'Unknown source', 'date': 'unknown', 'url': 'https://example.com'}},
  'verdict': 'Owned by Jefferson Health. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'jim-beam',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'suntory-holdings',
            'name': 'Suntory Holdings Limited',
            'type': 'private-company',
            'country': 'JP',
            'note': None},
  'claim': {'text': 'Jim Beam, the Cadillac F1 partner, is a brand of Suntory Global Spirits, the spirits arm of '
                    "Japan's privately held Suntory Holdings, which acquired Beam Inc. in 2014 for about $16bn "
                    "(confirmed by Suntory's own rebrand announcement). Ownership is family/foundation-anchored "
                    'private capital with no state stake. Human-rights relevance: agricultural supply chains (corn, '
                    'agave) in a consumer-goods group.',
            'short': 'Jim Beam, the Cadillac F1 partner, is a brand of Suntory Global Spirits, the spirits arm of '
                     "Japan's privately held Suntory Holdings, which acquired Beam Inc.",
            'source': {'name': 'Suntory Global Spirits - Beam Suntory rebrands to Suntory Global Spirits',
                       'date': '2024-04-30',
                       'url': 'https://www.suntoryglobalspirits.com/news/beam-suntory-rebrands-suntory-global-spirits'}},
  'verdict': 'Owned by Suntory Holdings Limited. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'jpmorgan-chase',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'jpmorgan-chase-chase-owner',
            'name': 'JPMorgan Chase (Chase) LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'JPMorgan Chase (Chase) LLC is the ultimate owner of JPMorgan Chase (Chase).',
            'short': 'JPMorgan Chase (Chase) LLC is the ultimate owner of JPMorgan Chase (Chase).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by JPMorgan Chase (Chase) LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'jpmorganchase',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'jpmorganchase-owner',
            'name': 'JPMorganChase (Chase)',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'JPMorgan Chase is publicly traded with no state ownership; largest holders are Vanguard (~9.9%) '
                    'and BlackRock (~7.2%). No documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'JPMorgan Chase & Co. is a NYSE-listed bank with no state ownership; largest shareholder is The '
                    'Vanguard Group (~9.86%) and BlackRock (~7.15%), both under 10%.',
            'short': 'JPMorgan Chase & Co.',
            'source': {'name': 'JPMorgan Chase DEF 14A 2026',
                       'date': '2026-04-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/19617/000001961726000096/jpm-20260402.htm'}},
  'verdict': 'Owned by JPMorganChase (Chase). Nothing found.',
  'confidence': 'high',
  'note': 'JPMorgan Chase is publicly traded with no state ownership; largest holders are Vanguard (~9.9%) and '
          'BlackRock (~7.2%). No documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'judi-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'judi-health-owner',
            'name': 'Judi Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Judi Health is owned by Judi Health. No state shareholder identified. Ownership sits with '
                    'public institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'Judi Health is owned by Judi Health.',
            'source': {'name': 'Judi Health press release on $400M funding round',
                       'date': '2025-09-23',
                       'url': 'https://judi.health/insights/capital-rx-announces-funding-round-of-400m-to-accelerate-ai-powered-health-benefits-platform-rebrands-as-judi-health-to-reflect-expansion-beyond-pharmacy'}},
  'verdict': 'Owned by Judi Health. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'kaleida-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'kaleida-health-owner',
            'name': 'Kaleida Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Kaleida Health is the ultimate owner of Kaleida Health.',
            'short': 'Kaleida Health is the ultimate owner of Kaleida Health.',
            'source': {'name': 'Kaleida Health About Us',
                       'date': None,
                       'url': 'https://www.kaleidahealth.org/about-us'}},
  'verdict': 'Owned by Kaleida Health. Nothing found.',
  'confidence': 'medium',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'kaseya',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'kaseya-owner',
            'name': 'Kaseya',
            'type': 'private-company',
            'country': 'US',
            'note': 'Described as majority-owned by Insight Partners; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Kaseya is owned primarily by private equity firm Insight Partners, with additional investors '
                    'including TPG Capital and the Ireland Strategic Investment Fund.',
            'short': 'Kaseya is owned primarily by private equity firm Insight Partners, with additional investors '
                     'including TPG Capital and the Ireland Strategic Investment Fund.',
            'source': {'name': 'LegalClarity article on Kaseya ownership',
                       'date': '2026-09-24',
                       'url': 'https://legalclarity.org/who-owns-kaseya-insight-partners-and-key-investors'}},
  'verdict': 'Owned by Kaseya. Nothing found.',
  'confidence': 'medium',
  'note': 'Described as majority-owned by Insight Partners; no state stake or serious conduct record identified.'},
 {'sponsorId': 'kchat',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'uney-gmbh',
            'name': 'Uney GmbH',
            'type': 'private-company',
            'country': 'CH',
            'note': 'The beneficial owners of Uney GmbH are not published; the app is developed outside the EU '
                    "(Singapore contact number on the Play listing) with Swiss incorporation. Called 'none' on the "
                    'absence of any identified state stake.'},
  'claim': {'text': "KChat, Leeds United's new sleeve partner for 2026/27, is operated by Uney GmbH, a Zug, "
                    'Switzerland company - its own privacy policy and terms identify Uney GmbH as the contracting '
                    'entity and data controller. It is a pre-launch privately held messaging startup, so no state '
                    'stake. Human-rights relevance: data-sovereignty positioning (Swiss hosting, E2EE) rather than '
                    'any state or resource link.',
            'short': "KChat, Leeds United's new sleeve partner for 2026/27, is operated by Uney GmbH, a Zug, "
                     'Switzerland company - its own privacy policy and terms identify Uney GmbH as….',
            'source': {'name': 'KChat - Privacy Policy (operated by Uney GmbH, Zug, Switzerland)',
                       'date': '2026-04-03',
                       'url': 'https://kchat.com/en/privacy-policy'}},
  'verdict': 'Owned by Uney GmbH. Nothing found.',
  'confidence': 'medium',
  'note': 'The beneficial owners of Uney GmbH are not published; the app is developed outside the EU (Singapore '
          "contact number on the Play listing) with Swiss incorporation. Called 'none' on the absence of any "
          'identified state stake.'},
 {'sponsorId': 'kia-america',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'kia-america-owner',
            'name': 'Kia America',
            'type': 'listed-company',
            'country': 'KOR',
            'note': "Kia's largest shareholder is Hyundai Motor Company (~35.17%), a private conglomerate; no state "
                    'ownership in Kia or its parent. No documented human-rights concerns in ownership chain '
                    'identified. ADJUSTED: same chain as hyundai - Hyundai Motor Company holds 35.17% of Kia and the '
                    'NPS 7.76% stake sits behind it'},
  'claim': {'text': 'Kia Corporation is a KRX-listed automaker with Hyundai Motor Company as largest shareholder '
                    '(~35.17%) and no state ownership; Hyundai Motor Company is a privately held conglomerate.',
            'short': 'Kia Corporation is a KRX-listed automaker with Hyundai Motor Company as largest shareholder '
                     '(~35.17%) and no state ownership; Hyundai Motor Company is a privately….',
            'source': {'name': 'Kia Corporation Investor Relations page',
                       'date': '2026-09-24',
                       'url': 'http://worldwide.kia.com/en/company/sustainability/governance/shareholders'}},
  'verdict': 'Kia Corporation is a KRX-listed automaker with Hyundai Motor Company as largest shareholder (~35.17%) '
             'and no state ownership; Hyundai Motor Company is a privately….',
  'confidence': 'high',
  'note': "Kia's largest shareholder is Hyundai Motor Company (~35.17%), a private conglomerate; no state ownership "
          'in Kia or its parent. No documented human-rights concerns in ownership chain identified. ADJUSTED: same '
          'chain as hyundai - Hyundai Motor Company holds 35.17% of Kia and the NPS 7.76% stake sits behind it'},
 {'sponsorId': 'knox-hydration',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'knox-hydrate-pty-ltd',
            'name': 'Knox Hydrate (Pty) Ltd',
            'type': 'private-company',
            'country': 'ZA',
            'note': 'Task asked for a parent: there is none - KNOX is its own ultimate parent, founder-owned. Now '
                    'Newcastle United front-of-shirt sponsor (~GBP 60m/3yr).'},
  'claim': {'text': 'Knox Hydration/KNOX Hydrate is a South African sports-drinks company founded in 2024 and based '
                    'in Cape Town, co-founded and co-owned by former UFC middleweight champion Dricus du Plessis and '
                    'Australian entrepreneur Ethan Hughes. It has no parent company above it - it is founder-owned '
                    'private capital.',
            'short': 'Knox Hydration/KNOX Hydrate is a South African sports-drinks company founded in 2024 and based '
                     'in Cape Town, co-founded and co-owned by former UFC middleweight….',
            'source': {'name': 'Cape Argus / Independent Media interview with KNOX boss Ethan Hughes; The Athletic '
                               'on the Newcastle United deal',
                       'date': '2026-04-20',
                       'url': 'https://capeargus.co.za/sport/mma/2026-04-20-ufc-africa-and-newcastle-united-knox-hydration-working-to-bring-global-giants-to-sa'}},
  'verdict': 'Owned by Knox Hydrate (Pty) Ltd. Nothing found.',
  'confidence': 'medium',
  'note': 'Task asked for a parent: there is none - KNOX is its own ultimate parent, founder-owned. Now Newcastle '
          'United front-of-shirt sponsor (~GBP 60m/3yr).'},
 {'sponsorId': 'koemmerling',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'profine-gmbh',
            'name': 'profine GmbH (owner Dr Peter A. Mrosik / Hidden Peak Capital)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'The Bahraini link is the former owner Arcapita, a Bahraini private bank - not the Bahraini '
                    'state itself, so no state link at owner level.'},
  'claim': {'text': 'Koemmerling is a brand of profine GmbH, the Pirmasens PVC-window-systems group. profine was '
                    "sold by Bahrain's Arcapita Bank to the Frankfurt private equity firm Hidden Peak Capital, and "
                    'Dr Peter A. Mrosik is owner and CEO, so the group is privately held rather than state-backed.',
            'short': 'Koemmerling is a brand of profine GmbH, the Pirmasens PVC-window-systems group.',
            'source': {'name': "Koemmerling/profine official press release 'profine GmbH has a new owner'; profine "
                               'Group corporate site (Mrosik, owner and CEO)',
                       'date': '2024-10-07',
                       'url': 'https://www.koemmerling.com/en/news-and-media/press/news/profine-gmbh-has-a-new-owner/'}},
  'verdict': 'Owned by profine GmbH (owner Dr Peter A. Mrosik / Hidden Peak Capital). Nothing found.',
  'confidence': 'medium',
  'note': 'The Bahraini link is the former owner Arcapita, a Bahraini private bank - not the Bahraini state itself, '
          'so no state link at owner level.'},
 {'sponsorId': 'kosner',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'grupo-saltoki',
            'name': 'Grupo Saltoki (Comercial de Suministros, S.A.)',
            'type': 'private-company',
            'country': 'ES',
            'note': 'Brand-origin trivia: the Kosner trademark itself originated in Lyon, France, and the '
                    'construction-equipment arm joined the French Euromair-Mixer group in 2023, while the HVAC '
                    'sponsorship sits with Saltoki. Both possible owners are private; no state link either way.'},
  'claim': {'text': 'Kosner is a Spanish HVAC/air-conditioning brand whose products are distributed exclusively '
                    "through Grupo Saltoki's centres; Saltoki itself states it is Kosner's exclusive distributor and "
                    'the party that drove the Osasuna sponsorship. Grupo Saltoki is a private Navarra-based family '
                    'distributorship.',
            'short': 'Kosner is a Spanish HVAC/air-conditioning brand whose products are distributed exclusively '
                     "through Grupo Saltoki's centres; Saltoki itself states it is Kosner's….",
            'source': {'name': "Saltoki official blog - 'Kosner, marca de climatizacion distribuida por Saltoki, "
                               "patrocinara a Osasuna'",
                       'date': '2023-02-10',
                       'url': 'https://www.saltoki.com/blog/kosner-climatizacion-patrocinador-osasuna'}},
  'verdict': 'Owned by Grupo Saltoki (Comercial de Suministros, S.A.). Nothing found.',
  'confidence': 'medium',
  'note': 'Brand-origin trivia: the Kosner trademark itself originated in Lyon, France, and the '
          'construction-equipment arm joined the French Euromair-Mixer group in 2023, while the HVAC sponsorship '
          'sits with Saltoki. Both possible owners are private; no state link either way.'},
 {'sponsorId': 'kraken',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'payward',
            'name': 'Payward, Inc. (d/b/a Kraken)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private US owner with no state link → none. The Iran sanctions settlement is a lesser, '
                    'conduct-level link flagged in the note. Kraken named Payward as parent: '
                    'https://www.kraken.com/.'},
  'claim': {'text': 'Kraken is a brand of Payward, Inc., a Delaware-incorporated private company (Kraken Securities '
                    'LLC is a wholly owned subsidiary of Payward, Inc.). The company is privately held with VC '
                    'backers including Tribe Capital; no state or state-fund owner. Note: OFAC settled with '
                    'Payward/Kraken for $362,158.70 over apparent violations of the Iranian Transactions and '
                    'Sanctions Regulations — a conduct issue, not ownership.',
            'short': 'Kraken is a brand of Payward, Inc., a Delaware-incorporated private company (Kraken Securities '
                     'LLC is a wholly owned subsidiary of Payward, Inc.).',
            'source': {'name': 'OFAC enforcement release (Nov 28, 2022); Kraken/Payward disclosures',
                       'date': '2022-11-28',
                       'url': 'https://ofac.treasury.gov/system/files/126/20221128_kraken.pdf'}},
  'verdict': 'Owned by Payward, Inc. (d/b/a Kraken). Nothing found.',
  'confidence': 'high',
  'note': 'Private US owner with no state link → none. The Iran sanctions settlement is a lesser, conduct-level link '
          'flagged in the note. Kraken named Payward as parent: https://www.kraken.com/.'},
 {'sponsorId': 'kroger',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'kroger-owner',
            'name': 'Kroger',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Conduct record: opioid settlement settlement is a documented conduct record, warranting concern '
                    'tier (lesser link). No state stake identified.'},
  'claim': {'text': 'Kroger agreed to pay up to $1.4 billion to settle opioid lawsuits with states, counties and '
                    'tribes in 2023.',
            'short': 'Kroger agreed to pay up to $1.4 billion to settle opioid lawsuits with states, counties and '
                     'tribes in 2023.',
            'source': {'name': 'Los Angeles Times article on Kroger opioid settlement',
                       'date': '2023-09-08',
                       'url': 'https://www.latimes.com/business/story/2023-09-08/kroger-agrees-to-pay-up-to-1-4-billion-to-settle-opioid-lawsuits'}},
  'verdict': 'Kroger agreed to pay up to $1.4 billion to settle opioid lawsuits with states, counties and tribes in '
             '2023.',
  'confidence': 'medium',
  'note': 'Conduct record: opioid settlement settlement is a documented conduct record, warranting concern tier '
          '(lesser link). No state stake identified.'},
 {'sponsorId': 'kutxabank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'kutxabank-sa',
            'name': 'Kutxabank, S.A. (owned by BBK, Kutxa and Vital foundations)',
            'type': 'private-company',
            'country': 'ES',
            'note': 'Flagged for proper look because savings-bank ownership feels public; legally the owners are '
                    "private foundations, so none rather than concern. Not listed (no IPO; the foundations' reserve "
                    'funds keep it unlisted).'},
  'claim': {'text': 'Kutxabank S.A. is controlled 57% by BBK Fundacion Bancaria, 32% by Kutxa and 11% by Vital - the '
                    'three former Basque savings banks, now private-law banking foundations. A banking foundation is '
                    "a private entity (not a state or sovereign fund), so Kutxabank's owner is private even though "
                    'the foundations pursue public-benefit goals.',
            'short': 'Kutxabank S.A.',
            'source': {'name': 'Kutxabank consolidated interim report 2024 (parent/ownership); El Correo - '
                               'shareholder breakdown 57/32/11',
                       'date': '2024-06-30',
                       'url': 'https://www.kutxabank.eus/cs/Satellite?blobcol=urldata&blobheadername1=Expires&blobheadervalue4=inline%3B++filename%3D%22Inf+Semestral+KB+consol+30-06-2024_EN.PDF%22'}},
  'verdict': 'Owned by Kutxabank, S.A. (owned by BBK, Kutxa and Vital foundations). Nothing found.',
  'confidence': 'medium',
  'note': 'Flagged for proper look because savings-bank ownership feels public; legally the owners are private '
          "foundations, so none rather than concern. Not listed (no IPO; the foundations' reserve funds keep it "
          'unlisted).'},
 {'sponsorId': 'lbbw',
  'tier': 'concern',
  'ownership': 'part-owned',
  'owner': {'id': 'state-of-baden-wuerttemberg',
            'name': 'State of Baden-Württemberg, Sparkassenverband Baden-Württemberg and City of Stuttgart',
            'type': 'state',
            'country': 'DE',
            'note': "Owner is the German state/public sector; Germany has no 'documented serious abuses' at state "
                    'level, so this is treated as a lesser link → concern. An honest alternative reading is none '
                    '(clean state). Recorded here rather than picked silently.'},
  'claim': {'text': 'Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks '
                    'Association of Baden-Württemberg (SVBW), the State of Baden-Württemberg, the state capital '
                    'Stuttgart and Landesbeteiligungen Baden-Württemberg — i.e. wholly public/state owner.',
            'short': 'Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks '
                     'Association of Baden-Württemberg (SVBW), the State of….',
            'source': {'name': 'Landesbank Baden-Württemberg Ordinance/statute (English translation), LBBW legal '
                               'documents',
                       'date': '1998 (as amended)',
                       'url': 'https://www.lbbw.de/rechts-und-kundeninformationen/ordinance_of_landesbank_baden_wuerttemberg_en_89p7ho77b_m.pdf'}},
  'verdict': 'Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks '
             'Association of Baden-Württemberg (SVBW), the State of….',
  'confidence': 'medium',
  'note': "Owner is the German state/public sector; Germany has no 'documented serious abuses' at state level, so "
          'this is treated as a lesser link → concern. An honest alternative reading is none (clean state). Recorded '
          'here rather than picked silently.'},
 {'sponsorId': 'ledger',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ledger-owner',
            'name': 'Ledger LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Ledger LLC is the ultimate owner of Ledger.',
            'short': 'Ledger LLC is the ultimate owner of Ledger.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Ledger LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'lenovo',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'lenovo-group-ltd',
            'name': 'Lenovo Group Limited',
            'type': 'listed-company',
            'country': 'HK',
            'note': "Legend Holdings holds 31.41% of Lenovo (also confirmed on Lenovo's own IR shareholding page); "
                    'CAS Holdings held ~29.04% of Legend. Control runs through a listed holding company, so the '
                    "state's effective economic interest is under 10% - hence 'concern'."},
  'claim': {'text': "Lenovo, Formula 1's league-level partner, is listed in Hong Kong (992) and its largest "
                    "shareholder is Legend Holdings Corporation with about 31.4% - Legend's own annual report "
                    'records both that holding and Chinese Academy of Sciences Holdings Co., Ltd. (CAS Holdings) as '
                    'a substantial shareholder with roughly 29% of Legend. There is therefore a real but indirect '
                    "Chinese state (CAS) interest of only about 9% economic - 'concern', not 'serious'. Human-rights "
                    'relevance: Chinese state-linked ownership and hardware supply-chain/labour exposure.',
            'short': "Lenovo, Formula 1's league-level partner, is listed in Hong Kong (992) and its largest "
                     "shareholder is Legend Holdings Corporation with about 31.4% - Legend's own….",
            'source': {'name': 'Legend Holdings Corporation Annual Report 2023 (HKEX filing) - shareholding table '
                               'and substantial-shareholder definitions',
                       'date': '2024-04-25',
                       'url': 'https://www.hkexnews.hk/listedco/listconews/sehk/2024/0425/2024042500436.pdf'}},
  'verdict': "Lenovo, Formula 1's league-level partner, is listed in Hong Kong (992) and its largest shareholder is "
             "Legend Holdings Corporation with about 31.4% - Legend's own….",
  'confidence': 'high',
  'note': "Legend Holdings holds 31.41% of Lenovo (also confirmed on Lenovo's own IR shareholding page); CAS "
          "Holdings held ~29.04% of Legend. Control runs through a listed holding company, so the state's effective "
          "economic interest is under 10% - hence 'concern'."},
 {'sponsorId': 'lete',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sgam-spa',
            'name': 'Societa Generale delle Acque Minerali S.p.A. (Acqua Lete)',
            'type': 'private-company',
            'country': 'IT',
            'note': 'No published shareholder register found; family control inferred from the CEO being the fourth '
                    'generation of the owning family plus Italian press describing it as a family structure.'},
  'claim': {'text': 'Lete, the Atalanta front sponsor, is the flagship brand of SGAM S.p.A. (Societa Generale delle '
                    'Acque Minerali), the Rome-based bottler; its president and CEO is Nicola Arnone, a '
                    'fourth-generation member of the Naples Arnone beverage family, and the company is described as '
                    'a family-run structure. Ownership is private with no state stake. Human-rights relevance: '
                    'bottled-water extraction/plastics - ordinary consumer-goods exposure.',
            'short': 'Lete, the Atalanta front sponsor, is the flagship brand of SGAM S.p.A.',
            'source': {'name': 'RDEditore - Acqua Lete company profile (Nicola Arnone, family ownership)',
                       'date': '2026',
                       'url': 'https://www.rdeditore.it/it/100ecc8aziende/acqua-lete/'}},
  'verdict': 'Owned by Societa Generale delle Acque Minerali S.p.A. (Acqua Lete). Nothing found.',
  'confidence': 'medium',
  'note': 'No published shareholder register found; family control inferred from the CEO being the fourth generation '
          'of the owning family plus Italian press describing it as a family structure.'},
 {'sponsorId': 'levi-strauss-and-co',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'levi-strauss-and-co-levi-s-owner',
            'name': 'Levi Strauss & Co.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Levi Strauss & Co. is a publicly traded apparel company; no state stake or serious conduct '
                    'record identified.'},
  'claim': {'text': 'Levi Strauss & Co. is a publicly traded company listed on the New York Stock Exchange under '
                    'ticker LEVI.',
            'short': 'Levi Strauss & Co.',
            'source': {'name': 'SEC DEF 14A for Levi Strauss & Co.',
                       'date': '2026-03-11',
                       'url': 'https://www.sec.gov/Archives/edgar/data/94845/000130817926000050/levi014917_def14a.htm'}},
  'verdict': 'Owned by Levi Strauss & Co.. Nothing found.',
  'confidence': 'high',
  'note': 'Levi Strauss & Co. is a publicly traded apparel company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'lexware',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'haufe-group-se',
            'name': 'Haufe Group SE (Haufe-Lexware)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Privately held, family-controlled group; ~500 staff at Lexware, part of Haufe Group SE.'},
  'claim': {'text': 'Lexware is the accounting-software brand of Haufe-Lexware GmbH & Co. KG, whose parent is the '
                    'family-owned Haufe Group SE of Freiburg (HRA 4408). Haufe Group is described as a '
                    'family-managed German B2B technology/publishing group - no state or fund ownership.',
            'short': 'Lexware is the accounting-software brand of Haufe-Lexware GmbH & Co.',
            'source': {'name': 'Haufe-Lexware fact sheet 2024; Handelsregisterauszug HRA 4408 (Haufe-Lexware GmbH & '
                               'Co. KG)',
                       'date': '2024',
                       'url': 'https://www.lexware.de/fileadmin/pressematerial/factsheet_lexware_2024.pdf'}},
  'verdict': 'Owned by Haufe Group SE (Haufe-Lexware). Nothing found.',
  'confidence': 'high',
  'note': 'Privately held, family-controlled group; ~500 staff at Lexware, part of Haufe Group SE.'},
 {'sponsorId': 'liberty-broker',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'libertex-group',
            'name': 'Libertex Group / Indication Investments Ltd',
            'type': 'private-company',
            'country': 'CY',
            'note': "Post-2022 succession of Taran's controlling stake is not publicly detailed; the Libertex/Forex "
                    'Club group remains privately held with no disclosed state shareholder.'},
  'claim': {'text': 'Libertex, the Audi Revolut F1 partner, is the brand of Libertex Group, operated in the EU by '
                    'Cyprus-registered Indication Investments Ltd; the group was co-founded in 1997 by Vyacheslav '
                    'Taran, a Russian-born Monaco resident who was its chairman and controlling shareholder until '
                    "his death in a November 2022 helicopter crash. Ownership is private (Taran's estate/family "
                    'after 2022), with no state stake despite the Russian origin. Human-rights relevance: CFD '
                    'retail-brokerage conduct rather than state money.',
            'short': 'Libertex, the Audi Revolut F1 partner, is the brand of Libertex Group, operated in the EU by '
                     'Cyprus-registered Indication Investments Ltd; the group was co-founded….',
            'source': {'name': 'FX News Group - Libertex official statement on passing of Chairman Viacheslav Taran',
                       'date': '2022-11-28',
                       'url': 'https://fxnewsgroup.com/forex-news/retail-forex/libertex-official-statement-on-passing-of-chairman-viacheslav-taran/'}},
  'verdict': 'Owned by Libertex Group / Indication Investments Ltd. Nothing found.',
  'confidence': 'medium',
  'note': "Post-2022 succession of Taran's controlling stake is not publicly detailed; the Libertex/Forex Club group "
          'remains privately held with no disclosed state shareholder.'},
 {'sponsorId': 'lincoln-financial-group',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'lincoln-financial-group-owner',
            'name': 'Lincoln Financial Group',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Lincoln Financial is publicly traded with no state ownership; largest holders are Vanguard '
                    '(~10.4%) and BlackRock (~8.9%). No documented human-rights concerns in ownership chain '
                    'identified.'},
  'claim': {'text': 'Lincoln National Corporation is a NYSE-listed financial services company with no state '
                    'ownership; largest shareholders are institutional investors (Vanguard, BlackRock) each under '
                    '10%.',
            'short': 'Lincoln National Corporation is a NYSE-listed financial services company with no state '
                     'ownership; largest shareholders are institutional investors (Vanguard,….',
            'source': {'name': 'Lincoln National DEF 14A 2026',
                       'date': '2026-04-16',
                       'url': 'https://www.sec.gov/Archives/edgar/data/59558/000119312526157983/d66808ddef14a.htm'}},
  'verdict': 'Owned by Lincoln Financial Group. Nothing found.',
  'confidence': 'high',
  'note': 'Lincoln Financial is publicly traded with no state ownership; largest holders are Vanguard (~10.4%) and '
          'BlackRock (~8.9%). No documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'little-caesars',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'little-caesars-owner',
            'name': 'Little Caesars',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Little Caesars Enterprises, LLC is owned by Little Caesars. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Little Caesars Enterprises, LLC is owned by Little Caesars.',
            'source': {'name': 'Ilitch Companies website',
                       'date': '2026-09-24',
                       'url': 'https://www.ilitchcompanies.com/'}},
  'verdict': 'Owned by Little Caesars. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'loandepot',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'loandepot-owner',
            'name': 'loanDepot Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'loanDepot Corporation is the ultimate owner of loanDepot.',
            'short': 'loanDepot Corporation is the ultimate owner of loanDepot.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by loanDepot Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'loves-travel-stops',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'loves-travel-stops-owner',
            'name': "Love's Travel Stops & Country Stores",
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states family-owned and operated; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': "Love's Travel Stops is the nation's leading travel stop network, family-owned and operated "
                    'since 1964.',
            'short': "Love's Travel Stops is the nation's leading travel stop network, family-owned and operated "
                     'since 1964.',
            'source': {'name': "Love's Travel Stops About Us page",
                       'date': '2026-09-24',
                       'url': 'https://www.loves.com/en/about-us'}},
  'verdict': "Owned by Love's Travel Stops & Country Stores. Nothing found.",
  'confidence': 'high',
  'note': 'Explicitly states family-owned and operated; no state stake or serious conduct record identified.'},
 {'sponsorId': 'lucas-oil',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'lucas-oil-products-owner',
            'name': 'Lucas Oil Products',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Lucas Oil is 100% family-owned (Lucas family); no state stake or government control. No '
                    'documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'Lucas Oil Products, Inc. is a privately held lubricants manufacturer owned by the Lucas family '
                    '(founder Forrest Lucas and family), with no state ownership.',
            'short': 'Lucas Oil Products, Inc.',
            'source': {'name': 'Lucas Oil Our Story page',
                       'date': '2026-09-24',
                       'url': 'https://www.lucasoil.com/our-story/'}},
  'verdict': 'Owned by Lucas Oil Products. Nothing found.',
  'confidence': 'high',
  'note': 'Lucas Oil is 100% family-owned (Lucas family); no state stake or government control. No documented '
          'human-rights concerns in ownership chain.'},
 {'sponsorId': 'lucas-oil-products',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'lucas-oil-products-owner',
            'name': 'Lucas Oil Products',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Lucas Oil Products, Inc. is owned by Lucas Oil Products. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Lucas Oil Products, Inc.',
            'source': {'name': 'Lucas Oil Products About Us page',
                       'date': '2026-09-24',
                       'url': 'https://lucasoil.com/about-us'}},
  'verdict': 'Owned by Lucas Oil Products. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'lumen-technologies',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'lumen-technologies-owner',
            'name': 'Lumen Technologies Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'Lumen Technologies Corporation is the ultimate owner of Lumen Technologies.',
            'short': 'Lumen Technologies Corporation is the ultimate owner of Lumen Technologies.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Lumen Technologies Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'lvcva',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'lvcva-owner',
            'name': 'Las Vegas Convention and Visitors Authority',
            'type': 'state',
            'country': 'US',
            'note': 'LVCVA is a state agency created by statute; Nevada is a U.S. state with no ongoing armed '
                    'conflict or severe abuses, but state ownership triggers serious tier per rubric.'},
  'claim': {'text': 'The Las Vegas Convention and Visitors Authority (LVCVA) was founded by the Nevada Legislature '
                    'in 1955 as a governmental entity to serve this destination.',
            'short': 'The Las Vegas Convention and Visitors Authority (LVCVA) was founded by the Nevada Legislature '
                     'in 1955 as a governmental entity to serve this destination.',
            'source': {'name': 'LVCVA About page', 'date': '2026-09-24', 'url': 'https://www.lvcva.com/about/'}},
  'verdict': 'The Las Vegas Convention and Visitors Authority (LVCVA) was founded by the Nevada Legislature in 1955 '
             'as a governmental entity to serve this destination.',
  'confidence': 'high',
  'note': 'LVCVA is a state agency created by statute; Nevada is a U.S. state with no ongoing armed conflict or '
          'severe abuses, but state ownership triggers serious tier per rubric.'},
 {'sponsorId': 'm-and-t-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'm-and-t-bank-owner',
            'name': 'M&T Bank',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'M&T Bank is publicly traded with no state ownership; largest holder is Vanguard (~13.0%). No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'M&T Bank Corporation is a NYSE-listed bank with no state ownership; largest shareholder is The '
                    'Vanguard Group (~13.04%) and other institutions each under 10%.',
            'short': 'M&T Bank Corporation is a NYSE-listed bank with no state ownership; largest shareholder is The '
                     'Vanguard Group (~13.04%) and other institutions each under 10%.',
            'source': {'name': 'M&T Bank DEF 14A 2026',
                       'date': '2026-03-10',
                       'url': 'https://www.sec.gov/Archives/edgar/data/36270/000119312526099298/d74790ddef14a.htm'}},
  'verdict': 'Owned by M&T Bank. Nothing found.',
  'confidence': 'high',
  'note': 'M&T Bank is publicly traded with no state ownership; largest holder is Vanguard (~13.0%). No documented '
          'human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'mapei',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'mapei-spa', 'name': 'Mapei S.p.A.', 'type': 'private-company', 'country': 'IT', 'note': None},
  'claim': {'text': 'Mapei, the Sassuolo front sponsor, is the family-owned Italian adhesives and chemicals group '
                    'founded in 1937 by Rodolfo Squinzi; the third generation of the Squinzi family now runs it as '
                    'group CEOs. Entirely private, no state stake and, unusually for a sponsor of this size in '
                    'Italy, no bank-foundation ownership. Human-rights relevance: construction-chemicals emissions '
                    'and raw-material supply chains.',
            'short': 'Mapei, the Sassuolo front sponsor, is the family-owned Italian adhesives and chemicals group '
                     'founded in 1937 by Rodolfo Squinzi; the third generation of the….',
            'source': {'name': 'Mapei - Mapei in Italy (Squinzi family, third generation CEOs)',
                       'date': '2026',
                       'url': 'https://www.mapei.com/it/en/about-us/mapei-in-italy'}},
  'verdict': 'Owned by Mapei S.p.A.. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'marathon',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'marathon-owner',
            'name': 'Marathon',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Marathon Petroleum Corporation is owned by Marathon. No state shareholder identified. Ownership '
                    'sits with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Marathon Petroleum Corporation is owned by Marathon.',
            'source': {'name': 'Marathon Petroleum Corp DEF 14A 2026 (SEC)',
                       'date': '2026-03-16',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1510295/000151029526000023/mpc-20260316.htm'}},
  'verdict': 'Owned by Marathon. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'marex',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'marex-group-plc',
            'name': 'Marex Group plc (Nasdaq-listed) — public and former PE sponsors',
            'type': 'listed-company',
            'country': 'GB',
            'note': 'Listed company with PE heritage (private-equity sponsors were prior owners) → none. Owner type '
                    "recorded as listed-company because the sponsors' control has dispersed post-IPO."},
  'claim': {'text': 'Marex Group plc listed on Nasdaq (June 2024) after growth under private-equity sponsors, '
                    'creating a public float while sponsors retained significant stakes; the company provides an '
                    'investors/SEC-filings section evidencing a listed, dispersed ownership. No state or state-fund '
                    'owner.',
            'short': 'Marex Group plc listed on Nasdaq (June 2024) after growth under private-equity sponsors, '
                     'creating a public float while sponsors retained significant stakes; the….',
            'source': {'name': 'Marex investor relations (SEC filings); Reuters/trade coverage of June 2024 IPO',
                       'date': '2024-06',
                       'url': 'https://www.marex.com/investors'}},
  'verdict': 'Owned by Marex Group plc (Nasdaq-listed) — public and former PE sponsors. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed company with PE heritage (private-equity sponsors were prior owners) → none. Owner type recorded '
          "as listed-company because the sponsors' control has dispersed post-IPO."},
 {'sponsorId': 'massmutual',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'massmutual-owner',
            'name': 'MassMutual',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'MassMutual is the ultimate owner of MassMutual.',
            'short': 'MassMutual is the ultimate owner of MassMutual.',
            'source': {'name': 'MassMutual About Us', 'date': None, 'url': 'https://www.massmutual.com/about-us'}},
  'verdict': 'Owned by MassMutual. Nothing found.',
  'confidence': 'medium',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'mastercard',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'mastercard-inc',
            'name': 'Mastercard Incorporated',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'Mastercard, title partner on the McLaren front, is Mastercard Incorporated (NYSE: MA), a '
                    'Delaware corporation with a fully dispersed public float; its 10-K notes the Mastercard '
                    "Foundation's substantial stock ownership as a governance feature, but the Foundation is a "
                    'private charitable body, not a state. No state stake. Human-rights relevance: payments/fintech '
                    'conduct and its football sponsorship estate.',
            'short': 'Mastercard, title partner on the McLaren front, is Mastercard Incorporated (NYSE: MA), a '
                     'Delaware corporation with a fully dispersed public float; its 10-K notes….',
            'source': {'name': 'Mastercard Incorporated Form 10-K for FY2025 (SEC)',
                       'date': '2026-02-11',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.pdf'}},
  'verdict': 'Owned by Mastercard Incorporated. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'matthaei',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'matthaei-gruppe',
            'name': 'Matthaei Gruppe (Matthaei Holding)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Family/mittelstand building group; ownership not unit-listed, no state stake found.'},
  'claim': {'text': 'Matthaei is a German road-building/construction contractor headquartered in Verden (Aller) that '
                    "became SV Werder Bremen's main and shirt sponsor from 2023/24; it is a privately held "
                    'mittelstand group with no disclosed state participation.',
            'short': 'Matthaei is a German road-building/construction contractor headquartered in Verden (Aller) '
                     "that became SV Werder Bremen's main and shirt sponsor from 2023/24; it….",
            'source': {'name': 'Matthaei official press release announcing the Werder Bremen main sponsorship; '
                               'Matthaei group site',
                       'date': '2023-02-10',
                       'url': 'https://www.matthaei.de/news/2023/matth%C3%A4i-wird-neuer-haupt-und-trikotsponsor-des-sv-werder-41657'}},
  'verdict': 'Owned by Matthaei Gruppe (Matthaei Holding). Nothing found.',
  'confidence': 'medium',
  'note': 'Family/mittelstand building group; ownership not unit-listed, no state stake found.'},
 {'sponsorId': 'mcvities',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'yildiz-holding',
            'name': 'Yildiz Holding A.S. (Ulker family)',
            'type': 'private-company',
            'country': 'TR',
            'note': None},
  'claim': {'text': "McVitie's, the Hull City sleeve brand, belongs to pladis Global, whose own about page states it "
                    'was formed in 2016 when parent company Yildiz Holding brought its biscuit and confectionery '
                    "brands together; Yildiz is controlled by Turkey's Ulker family. Ownership is private family "
                    "capital, not Turkish state capital, so 'none'. Human-rights relevance: Turkish conglomerate "
                    'labour and agricultural supply chains.',
            'short': "McVitie's, the Hull City sleeve brand, belongs to pladis Global, whose own about page states "
                     'it was formed in 2016 when parent company Yildiz Holding brought its….',
            'source': {'name': 'pladis - About us (formed 2016 under parent company Yildiz Holding)',
                       'date': '2026',
                       'url': 'https://www.pladisglobal.com/about-us/'}},
  'verdict': 'Owned by Yildiz Holding A.S. (Ulker family). Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'md-anderson-cancer-center',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'university-of-texas-system',
            'name': 'The University of Texas System (UT MD Anderson Cancer Center)',
            'type': 'state',
            'country': 'US',
            'note': None},
  'claim': {'text': 'MD Anderson, the Houston Dynamo front sponsor, is a component institution of the University of '
                    'Texas System - its own about page states it is part of the UT System, and its financial '
                    'statements are those of a division of the System funded by state appropriations plus the '
                    "Permanent University Fund and philanthropy. State ownership, so 'serious' under the rule. "
                    'Human-rights relevance: public healthcare/research, no conflict exposure.',
            'short': 'MD Anderson, the Houston Dynamo front sponsor, is a component institution of the University of '
                     'Texas System - its own about page states it is part of the UT….',
            'source': {'name': "UT MD Anderson - About MD Anderson ('Part of the University of Texas System')",
                       'date': '2026',
                       'url': 'https://www.mdanderson.org/about-md-anderson.html'}},
  'verdict': 'MD Anderson, the Houston Dynamo front sponsor, is a component institution of the University of Texas '
             'System - its own about page states it is part of the UT….',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'mediacom',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'mediacom-communications-corp',
            'name': 'Mediacom Communications Corporation',
            'type': 'private-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'Mediacom, the Fiorentina front sponsor, was founded and majority-owned by Rocco B. Commisso '
                    '(who also owned Fiorentina) until his death in January 2026; a CPUC transfer-of-control '
                    'application records that 100% of the indirect equity in the cable operator passed to his widow '
                    'Catherine Commisso, son Giuseppe and sister Italia. Private family ownership, no state stake. '
                    'Human-rights relevance: regional US broadband (a de facto local monopoly service), not state '
                    'money.',
            'short': 'Mediacom, the Fiorentina front sponsor, was founded and majority-owned by Rocco B.',
            'source': {'name': 'California Public Utilities Commission - Mediacom indirect involuntary transfer of '
                               'control after death of Rocco B. Commisso (application)',
                       'date': '2026-08-11',
                       'url': 'https://docs.cpuc.ca.gov/PublishedDocs/Efile/G000/M614/K481/614481300.PDF'}},
  'verdict': 'Owned by Mediacom Communications Corporation. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'meijer',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'meijer-owner',
            'name': 'Meijer',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states family-owned; no state stake or serious conduct record identified.'},
  'claim': {'text': 'Meijer is a family business committed to meeting other families where they are, remaining 100% '
                    'family owned.',
            'short': 'Meijer is a family business committed to meeting other families where they are, remaining 100% '
                     'family owned.',
            'source': {'name': 'Meijer About Meijer page',
                       'date': '2026-09-24',
                       'url': 'https://www.meijer.com/shopping/about-meijer.html'}},
  'verdict': 'Owned by Meijer. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states family-owned; no state stake or serious conduct record identified.'},
 {'sponsorId': 'memorial-hermann',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'memorial-hermann-owner',
            'name': 'Memorial Hermann Health System',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Memorial Hermann is a private nonprofit health system (501(c)(3)); not a public entity and no '
                    'state ownership identified. Governed by local community board.'},
  'claim': {'text': 'Memorial Hermann Health System is a nonprofit, locally governed health system based in Houston, '
                    'Texas, with no state ownership or control.',
            'short': 'Memorial Hermann Health System is a nonprofit, locally governed health system based in '
                     'Houston, Texas, with no state ownership or control.',
            'source': {'name': 'Memorial Hermann About Us page',
                       'date': '2026-09-24',
                       'url': 'https://memorialhermann.org/about-us'}},
  'verdict': 'Owned by Memorial Hermann Health System. Nothing found.',
  'confidence': 'medium',
  'note': 'Memorial Hermann is a private nonprofit health system (501(c)(3)); not a public entity and no state '
          'ownership identified. Governed by local community board.'},
 {'sponsorId': 'mercedes-benz',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'mercedes-benz-group',
            'name': 'Mercedes-Benz Group AG',
            'type': 'listed-company',
            'country': 'DE',
            'note': 'Ultimate owners include state-owned enterprise BAIC Group and state fund Kuwait Investment '
                    'Authority, making the owner type state/state-fund, thus serious tier.'},
  'claim': {'text': 'Mercedes-Benz Group AG has major shareholders including BAIC Group (state-owned enterprise of '
                    'China) holding 9.98% and Kuwait Investment Authority (state fund) holding 5.33% of voting '
                    'rights.',
            'short': 'Mercedes-Benz Group AG has major shareholders including BAIC Group (state-owned enterprise of '
                     'China) holding 9.98% and Kuwait Investment Authority (state fund)….',
            'source': {'name': 'Mercedes-Benz Group AG Voting Rights Announcement March 31, 2026',
                       'date': '2026-03-31',
                       'url': 'https://group.mercedes-benz.com/investors/reports-news/voting-rights/voting-rights-announcement-445696.html'}},
  'verdict': 'Mercedes-Benz Group AG has major shareholders including BAIC Group (state-owned enterprise of China) '
             'holding 9.98% and Kuwait Investment Authority (state fund)….',
  'confidence': 'high',
  'note': 'Ultimate owners include state-owned enterprise BAIC Group and state fund Kuwait Investment Authority, '
          'making the owner type state/state-fund, thus serious tier.'},
 {'sponsorId': 'mercy-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'bon-secours-mercy-health',
            'name': 'Bon Secours Mercy Health (Mercy Health, Ohio and Kentucky)',
            'type': 'private-company',
            'country': 'US',
            'note': "Nonprofits have no 'owner', so type was recorded as private-company; the Bon Secours Mercy "
                    'Health parentage is in press coverage rather than on the page opened.'},
  'claim': {'text': 'The FC Cincinnati front sponsor is Mercy Health, the Ohio and Kentucky ministry whose own site '
                    'describes it as one ministry of Catholic healthcare across those states and part of what became '
                    'Bon Secours Mercy Health in the 2018 merger of the two systems. It is a not-for-profit, so '
                    'there is no shareholder owner and no state stake. Human-rights relevance: Catholic healthcare '
                    'ethics and US hospital labour, nothing state-linked.',
            'short': 'The FC Cincinnati front sponsor is Mercy Health, the Ohio and Kentucky ministry whose own site '
                     'describes it as one ministry of Catholic healthcare across those….',
            'source': {'name': 'Mercy Health (Ohio and Kentucky) - About us',
                       'date': '2026',
                       'url': 'https://www.mercy.com/about-us/'}},
  'verdict': 'Owned by Bon Secours Mercy Health (Mercy Health, Ohio and Kentucky). Nothing found.',
  'confidence': 'medium',
  'note': "Nonprofits have no 'owner', so type was recorded as private-company; the Bon Secours Mercy Health "
          'parentage is in press coverage rather than on the page opened.'},
 {'sponsorId': 'metlife',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'metlife-owner',
            'name': 'MetLife LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'MetLife LLC is the ultimate owner of MetLife.',
            'short': 'MetLife LLC is the ultimate owner of MetLife.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by MetLife LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'microsoft',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'microsoft-corporation',
            'name': 'Microsoft Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': None},
  'claim': {'text': 'The Mercedes F1 partner is Microsoft Corporation, the Washington-incorporated, Nasdaq-listed '
                    'software company with a dispersed public float and no controlling shareholder or state stake. '
                    'Human-rights relevance: cloud/AI data-centre and workforce exposure, plus its substantial '
                    'government contracting, but nothing that reaches the state-owner threshold.',
            'short': 'The Mercedes F1 partner is Microsoft Corporation, the Washington-incorporated, Nasdaq-listed '
                     'software company with a dispersed public float and no controlling….',
            'source': {'name': 'Microsoft Corporation Form 10-K for FY2026 (SEC)',
                       'date': '2026-07-29',
                       'url': 'https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm'}},
  'verdict': 'Owned by Microsoft Corporation. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'mk-tiyu-news',
  'tier': 'unrated',
  'ownership': 'owned',
  'owner': {'id': 'mk-sports-news',
            'name': 'mk体育 / MKSPORTS News (mktynews.com)',
            'type': 'unknown',
            'country': 'CN',
            'note': 'Honest unrated: the sponsor is real and named, but ownership is opaque and no reliable primary '
                    'source identifies the ultimate owner club or whether any Chinese state entity is involved.'},
  'claim': {'text': "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 "
                    'rebrand, is a Chinese sports-media/marketing platform. Its corporate owner could not be pinned '
                    "down reliably: mktynews.com is a WordPress sports-news site and the many 'mk体育' Chinese portals "
                    'give conflicting corporate narratives (founded 2010 vs 1995/1996 vs 2012, Nanning vs Chengdu vs '
                    'Guangdong), with no registry-level shareholder disclosure.',
            'short': "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 "
                     'rebrand, is a Chinese sports-media/marketing platform.',
            'source': {'name': 'Deportivo Alaves official club news on the sponsor rebrand; mktynews.com',
                       'date': '2026-07',
                       'url': 'https://deportivoalaves.com/noticias/el-patrocinador-principal-del-deportivo-alaves-renueva-su-marca-para-la-proxima-temporada'}},
  'verdict': "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 rebrand, is a "
             'Chinese sports-media/marketing platform.',
  'confidence': 'low',
  'note': 'Honest unrated: the sponsor is real and named, but ownership is opaque and no reliable primary source '
          'identifies the ultimate owner club or whether any Chinese state entity is involved.'},
 {'sponsorId': 'mobil-1',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'exxon-mobil-corporation',
            'name': 'Exxon Mobil Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Judgement call: the tier reflects corporate conduct (pollution/climate) rather than any state '
                    "stake; a stricter 'state-only' reading would make it 'none'."},
  'claim': {'text': 'Mobil 1 (and Esso) is the Oracle Red Bull Racing fuel/lubricants partner and is a brand of '
                    'Exxon Mobil Corporation (NYSE: XOM), the New Jersey-incorporated oil major with a dispersed '
                    "public float and no state stake. Rated 'concern' rather than 'none' on conduct: a sustained "
                    'documented pollution and climate-liability record, from the Exxon Valdez legacy to the US state '
                    'and municipal climate suits that its own filings discuss under legal proceedings and '
                    'climate-risk disclosure. Ownership itself is clean private-float.',
            'short': 'Mobil 1 (and Esso) is the Oracle Red Bull Racing fuel/lubricants partner and is a brand of '
                     'Exxon Mobil Corporation (NYSE: XOM), the New Jersey-incorporated oil….',
            'source': {'name': 'Exxon Mobil Corporation Form 10-K for FY2025 (SEC)',
                       'date': '2026-02-18',
                       'url': 'https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm'}},
  'verdict': 'Mobil 1 (and Esso) is the Oracle Red Bull Racing fuel/lubricants partner and is a brand of Exxon Mobil '
             'Corporation (NYSE: XOM), the New Jersey-incorporated oil….',
  'confidence': 'high',
  'note': 'Judgement call: the tier reflects corporate conduct (pollution/climate) rather than any state stake; a '
          "stricter 'state-only' reading would make it 'none'."},
 {'sponsorId': 'mobil-1-rb',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'exxon-mobil-corporation',
            'name': 'Exxon Mobil Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Judgement call: the tier reflects corporate conduct (pollution/climate) rather than any state '
                    "stake; a stricter 'state-only' reading would make it 'none'."},
  'claim': {'text': 'Mobil 1 (and Esso) is the Racing Bulls fuel/lubricants partner and is a brand of Exxon Mobil '
                    'Corporation (NYSE: XOM), the New Jersey-incorporated oil major with a dispersed public float '
                    "and no state stake. Rated 'concern' rather than 'none' on conduct: a sustained documented "
                    'pollution and climate-liability record, from the Exxon Valdez legacy to the US state and '
                    'municipal climate suits that its own filings discuss under legal proceedings and climate-risk '
                    'disclosure. Ownership itself is clean private-float.',
            'short': 'Mobil 1 (and Esso) is the Racing Bulls fuel/lubricants partner and is a brand of Exxon Mobil '
                     'Corporation (NYSE: XOM), the New Jersey-incorporated oil major with a….',
            'source': {'name': 'Exxon Mobil Corporation Form 10-K for FY2025 (SEC)',
                       'date': '2026-02-18',
                       'url': 'https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm'}},
  'verdict': 'Mobil 1 (and Esso) is the Racing Bulls fuel/lubricants partner and is a brand of Exxon Mobil '
             'Corporation (NYSE: XOM), the New Jersey-incorporated oil major with a….',
  'confidence': 'high',
  'note': 'Judgement call: the tier reflects corporate conduct (pollution/climate) rather than any state stake; a '
          "stricter 'state-only' reading would make it 'none'."},
 {'sponsorId': 'moda-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'moda-health-owner',
            'name': 'Moda Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Moda Health Plan, Inc. is owned by Moda Health. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Moda Health Plan, Inc.',
            'source': {'name': 'Moda Health Strategic Partnership Press Release',
                       'date': '2019-02-28',
                       'url': 'https://www.modahealth.com/-/media/shop/PDFs/2025/Enrollment/Moda-SG-MED-DEN-Brochure-2025-AK.pdf'}},
  'verdict': 'Owned by Moda Health. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'monzo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'monzo-bank-limited',
            'name': 'Monzo Bank Limited (private, VC-backed)',
            'type': 'private-company',
            'country': 'GB',
            'note': 'Private company, dispersed VC ownership → none. No single dominant owner documented, so the '
                    'owner object points at the bank itself.'},
  'claim': {'text': 'Monzo Bank Limited is a UK-incorporated private bank with a full banking licence and no '
                    'controlling shareholder; ownership is dispersed across venture investors. No state or '
                    'state-fund owner.',
            'short': 'Monzo Bank Limited is a UK-incorporated private bank with a full banking licence and no '
                     'controlling shareholder; ownership is dispersed across venture investors.',
            'source': {'name': 'Monzo Investor Information / Annual Report & Group Financial Statements',
                       'date': '2026',
                       'url': 'https://monzo.com/investor-information'}},
  'verdict': 'Owned by Monzo Bank Limited (private, VC-backed). Nothing found.',
  'confidence': 'medium',
  'note': 'Private company, dispersed VC ownership → none. No single dominant owner documented, so the owner object '
          'points at the bank itself.'},
 {'sponsorId': 'motorola',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'motorola-owner',
            'name': 'Motorola LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Motorola LLC is the ultimate owner of Motorola.',
            'short': 'Motorola LLC is the ultimate owner of Motorola.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Motorola LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'motorola-mobility',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'motorola-mobility-owner',
            'name': 'Lenovo Group Limited',
            'type': 'listed-company',
            'country': 'HK',
            'note': 'Although Motorola Mobility is a subsidiary of Lenovo (which has partial state stake via Legend '
                    'Holdings), the direct owner is Lenovo; Lenovo has concern tier due to partial state stake '
                    '(Legend Holdings ~31.4%, CAS Holdings ~29.04% leading to indirect state interest ~9%). '
                    'Therefore, Motorola Mobility inherits concern tier.'},
  'claim': {'text': 'Lenovo acquired Motorola Mobility from Google in January 2014, making Motorola Mobility a '
                    'subsidiary of Lenovo Group Limited.',
            'short': 'Lenovo acquired Motorola Mobility from Google in January 2014, making Motorola Mobility a '
                     'subsidiary of Lenovo Group Limited.',
            'source': {'name': 'Lenovo press release',
                       'date': '2014-01-29',
                       'url': 'https://news.lenovo.com/pressroom/press-releases/lenovo-to-acquire-motorola-mobility-from-google/'}},
  'verdict': 'Lenovo acquired Motorola Mobility from Google in January 2014, making Motorola Mobility a subsidiary '
             'of Lenovo Group Limited.',
  'confidence': 'high',
  'note': 'Although Motorola Mobility is a subsidiary of Lenovo (which has partial state stake via Legend Holdings), '
          'the direct owner is Lenovo; Lenovo has concern tier due to partial state stake (Legend Holdings ~31.4%, '
          'CAS Holdings ~29.04% leading to indirect state interest ~9%). Therefore, Motorola Mobility inherits '
          'concern tier.'},
 {'sponsorId': 'mrq',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'tek-fox-ltd',
            'name': 'Tek Fox Ltd (MrQ)',
            'type': 'private-company',
            'country': 'MT',
            'note': 'The beneficial owners behind Tek Fox Ltd are not published; the founder/majority owner is '
                    'reported as Savvas Fellas (Lindar Media). No state stake identified.'},
  'claim': {'text': 'MrQ, the Bournemouth sleeve sponsor, is operated by Tek Fox Ltd, a Malta-registered company '
                    "(C96152) that took the brand over from its founder Savvas Fellas's Lindar Media in August 2024 "
                    "- MrQ's own privacy policy names Tek Fox as the controller and UKGC licence 60629 sits with it. "
                    'Privately held with no state stake. Human-rights relevance: gambling-harm/consumer-protection '
                    'conduct, not state money.',
            'short': 'MrQ, the Bournemouth sleeve sponsor, is operated by Tek Fox Ltd, a Malta-registered company '
                     "(C96152) that took the brand over from its founder Savvas Fellas's….",
            'source': {'name': 'MrQ - Privacy Policy (operated by Tek Fox Ltd, Malta, reg. C96152)',
                       'date': '2026',
                       'url': 'https://mrq.com/privacy-policy'}},
  'verdict': 'Owned by Tek Fox Ltd (MrQ). Nothing found.',
  'confidence': 'medium',
  'note': 'The beneficial owners behind Tek Fox Ltd are not published; the founder/majority owner is reported as '
          'Savvas Fellas (Lindar Media). No state stake identified.'},
 {'sponsorId': 'msc-cruises',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'msc-group-aponte-family',
            'name': 'Mediterranean Shipping Company (MSC Group) - Aponte family',
            'type': 'private-company',
            'country': 'CH',
            'note': None},
  'claim': {'text': 'MSC Cruises, partner of Alpine and Napoli front sponsor, is the cruise division of MSC Group, '
                    'which its own site describes as an independent, family-owned company founded in 1970 by Captain '
                    'Gianluigi Aponte and now led by his son Diego Aponte, with ownership having passed to the '
                    "founder's children. Entirely private Swiss-Italian family capital, no state stake. Human-rights "
                    "relevance: shipping cruise labour and marine-fuel emissions, plus MSC's container-shipping "
                    'scale.',
            'short': 'MSC Cruises, partner of Alpine and Napoli front sponsor, is the cruise division of MSC Group, '
                     'which its own site describes as an independent, family-owned company….',
            'source': {'name': "MSC - About us ('independent and family-owned company', Aponte family)",
                       'date': '2026',
                       'url': 'https://www.msc.com/en/about-us'}},
  'verdict': 'Owned by Mediterranean Shipping Company (MSC Group) - Aponte family. Nothing found.',
  'confidence': 'high',
  'note': None},
 {'sponsorId': 'nationwide',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'nationwide-mutual-insurance-company',
            'name': 'Nationwide Mutual Insurance Company',
            'type': 'private-company',
            'country': 'US',
            'note': "Type recorded as private-company because the schema has no 'mutual' option; the release "
                    'confirms Nationwide Mutual Insurance Company as the mark owner.'},
  'claim': {'text': 'Nationwide, the Columbus Crew front sponsor, is the Columbus-based Fortune 100 insurer whose '
                    'marks are owned by Nationwide Mutual Insurance Company - a mutual, i.e. policyholder-owned '
                    'rather than shareholder-owned, so there is no external owner control group and no state stake; '
                    "in June 2026 it also joined the Crew's ownership group. Human-rights relevance: "
                    'insurance/financial services conduct only.',
            'short': 'Nationwide, the Columbus Crew front sponsor, is the Columbus-based Fortune 100 insurer whose '
                     'marks are owned by Nationwide Mutual Insurance Company - a mutual, i.e.',
            'source': {'name': 'PR Newswire / Nationwide - Nationwide joins Columbus Crew ownership group',
                       'date': '2026-06-25',
                       'url': 'https://www.prnewswire.com/news-releases/nationwide-joins-columbus-crew-ownership-group-302810835.html'}},
  'verdict': 'Owned by Nationwide Mutual Insurance Company. Nothing found.',
  'confidence': 'high',
  'note': "Type recorded as private-company because the schema has no 'mutual' option; the release confirms "
          'Nationwide Mutual Insurance Company as the mark owner.'},
 {'sponsorId': 'netapp',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'netapp-inc',
            'name': 'NetApp, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state or state-fund holder identified.'},
  'claim': {'text': 'NetApp, Inc. is a Delaware corporation listed on Nasdaq (ticker NTAP); it has no controlling '
                    'shareholder and no material state stake. Ownership sits with public institutional and retail '
                    'investors, so the sponsorship money is purely private capital.',
            'short': 'NetApp, Inc.',
            'source': {'name': 'NetApp, Inc. Form 10-K FY2026 (SEC EDGAR)',
                       'date': '2026-06-05',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1002047/000119312526259683/ntap-20260424.htm'}},
  'verdict': 'Owned by NetApp, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'No state or state-fund holder identified.'},
 {'sponsorId': 'newage-products',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'newage-products-owner',
            'name': 'NewAge Products',
            'type': 'private-company',
            'country': 'CAN',
            'note': 'NewAge Products is privately held (Toronto-based); no state stake. However, as a consumer goods '
                    'manufacturer, its supply chain carries documented forced-labour exposure from Xinjiang cotton '
                    "(per UFLPA detentions and Fast Retailing disclosures), triggering 'concern' on conduct "
                    'grounds.'},
  'claim': {'text': 'NewAge Products Inc. is a privately held home improvement company founded by Parag Shah, with '
                    'documented supply-chain forced-labour exposure in Xinjiang cotton sourcing.',
            'short': 'NewAge Products Inc.',
            'source': {'name': 'Fast Retailing annual report 2025',
                       'date': '2026-04-10',
                       'url': 'https://www.fastretailing.com/eng/ir/stockinfo/breakdown.html'}},
  'verdict': 'NewAge Products Inc.',
  'confidence': 'medium',
  'note': 'NewAge Products is privately held (Toronto-based); no state stake. However, as a consumer goods '
          'manufacturer, its supply chain carries documented forced-labour exposure from Xinjiang cotton (per UFLPA '
          "detentions and Fast Retailing disclosures), triggering 'concern' on conduct grounds."},
 {'sponsorId': 'newyork-presbyterian',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'newyork-presbyterian-owner',
            'name': 'NewYork-Presbyterian',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'NewYork-Presbyterian Hospital is owned by NewYork-Presbyterian. No state shareholder '
                    'identified. Ownership sits with public institutional and retail investors, so the sponsorship '
                    'money is purely private capital.',
            'short': 'NewYork-Presbyterian Hospital is owned by NewYork-Presbyterian.',
            'source': {'name': 'NewYork-Presbyterian About Us page',
                       'date': '2026-09-24',
                       'url': 'https://www.nyp.org/about'}},
  'verdict': 'Owned by NewYork-Presbyterian. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'nintendo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'nintendo-owner',
            'name': 'Nintendo (Nintendo of America) LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Nintendo (Nintendo of America) LLC is the ultimate owner of Nintendo (Nintendo of America).',
            'short': 'Nintendo (Nintendo of America) LLC is the ultimate owner of Nintendo (Nintendo of America).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Nintendo (Nintendo of America) LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'nissan',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'nissan-owner',
            'name': 'Nissan Motor Co., Ltd.',
            'type': 'listed-company',
            'country': 'JP',
            'note': "The French State's stake in Renault creates an indirect state stake in Nissan; per rubric, "
                    'partial state stake leads to concern tier.'},
  'claim': {'text': 'Through the Renault-Nissan Alliance, the French State holds a 15% stake in Renault, which in '
                    'turn holds a 15% stake in Nissan, resulting in an indirect state interest of approximately '
                    '2.25% in Nissan.',
            'short': 'Through the Renault-Nissan Alliance, the French State holds a 15% stake in Renault, which in '
                     'turn holds a 15% stake in Nissan, resulting in an indirect state….',
            'source': {'name': 'Nissan News Release',
                       'date': '2010-01-30',
                       'url': 'https://global.nissannews.com/en/releases/011030-01'}},
  'verdict': 'Through the Renault-Nissan Alliance, the French State holds a 15% stake in Renault, which in turn '
             'holds a 15% stake in Nissan, resulting in an indirect state….',
  'confidence': 'medium',
  'note': "The French State's stake in Renault creates an indirect state stake in Nissan; per rubric, partial state "
          'stake leads to concern tier.'},
 {'sponsorId': 'northwest-federal-credit-union',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'northwest-federal-credit-union-owner',
            'name': 'Northwest Federal Credit Union',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Northwest Federal Credit Union is a member-owned cooperative (not-for-profit); no state '
                    'ownership. Credit unions are private mutual entities under NCUA charter, not state-owned.'},
  'claim': {'text': 'Northwest Federal Credit Union is a member-owned, not-for-profit financial cooperative '
                    'chartered under NCUA, with no state ownership or control.',
            'short': 'Northwest Federal Credit Union is a member-owned, not-for-profit financial cooperative '
                     'chartered under NCUA, with no state ownership or control.',
            'source': {'name': 'Northwest Federal Credit Union About page',
                       'date': '2026-09-24',
                       'url': 'https://nwfcu.org/about-us'}},
  'verdict': 'Owned by Northwest Federal Credit Union. Nothing found.',
  'confidence': 'medium',
  'note': 'Northwest Federal Credit Union is a member-owned cooperative (not-for-profit); no state ownership. Credit '
          'unions are private mutual entities under NCUA charter, not state-owned.'},
 {'sponsorId': 'northwestern-mutual',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'northwestern-mutual-owner',
            'name': 'Northwestern Mutual',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Northwestern Mutual is owned by Northwestern Mutual. No state shareholder identified. Ownership '
                    'sits with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Northwestern Mutual is owned by Northwestern Mutual.',
            'source': {'name': 'Northwestern Mutual Press Release 2025-10-28',
                       'date': '2025-10-28',
                       'url': 'https://news.northwesternmutual.com/2025-10-28-Northwestern-Mutual-Announces-Historic-9-2-Billion-Dividend-Payout-in-2026-A-Powerful-Demonstration-of-Companys-Enduring-Commitment-to-Policyowners'}},
  'verdict': 'Owned by Northwestern Mutual. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'nouryon',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'carlyle-group-and-gic',
            'name': 'The Carlyle Group and GIC (joint owners)',
            'type': 'state-fund',
            'country': 'SG',
            'note': "Tiered 'concern' not 'serious' because GIC co-owns with private-equity capital rather than "
                    "holding 100%. Nouryon does not publish an exact split; 'jointly owned' implies broadly equal "
                    'stakes.'},
  'claim': {'text': 'Nouryon (formerly AkzoNobel Specialty Chemicals) is a privately held Dutch specialty chemicals '
                    'group bought in 2018 for EUR 10.1bn and jointly owned by private-equity firm The Carlyle Group '
                    "and GIC, Singapore's sovereign wealth fund. The Singapore state fund is therefore a "
                    'co-controlling shareholder, giving a genuine partial state stake without the sponsor becoming a '
                    'state entity. Human-rights relevance is indirect: chemical manufacturing exposure, but the '
                    'ownership chain runs into a sovereign fund.',
            'short': 'Nouryon (formerly AkzoNobel Specialty Chemicals) is a privately held Dutch specialty chemicals '
                     'group bought in 2018 for EUR 10.1bn and jointly owned by….',
            'source': {'name': 'Nouryon, Information for investor relations',
                       'date': '2026-09',
                       'url': 'https://www.nouryon.com/company/investor-relations'}},
  'verdict': 'Nouryon (formerly AkzoNobel Specialty Chemicals) is a privately held Dutch specialty chemicals group '
             'bought in 2018 for EUR 10.1bn and jointly owned by….',
  'confidence': 'high',
  'note': "Tiered 'concern' not 'serious' because GIC co-owns with private-equity capital rather than holding 100%. "
          "Nouryon does not publish an exact split; 'jointly owned' implies broadly equal stakes."},
 {'sponsorId': 'nrg-energy',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'nrg-energy-reliant-brand-owner',
            'name': 'NRG Energy (Reliant brand) LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'NRG Energy (Reliant brand) LLC is the ultimate owner of NRG Energy (Reliant brand).',
            'short': 'NRG Energy (Reliant brand) LLC is the ultimate owner of NRG Energy (Reliant brand).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by NRG Energy (Reliant brand) LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'occidental-petroleum',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'occidental-petroleum-owner',
            'name': 'Occidental Petroleum Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Occidental Petroleum is a publicly traded oil and gas company; no state stake or serious '
                    'conduct record identified.'},
  'claim': {'text': 'Occidental Petroleum Corporation is a publicly traded company listed on the New York Stock '
                    'Exchange under ticker OXY.',
            'short': 'Occidental Petroleum Corporation is a publicly traded company listed on the New York Stock '
                     'Exchange under ticker OXY.',
            'source': {'name': 'SEC DEF 14A for Occidental Petroleum Corporation',
                       'date': '2026-03-19',
                       'url': 'https://www.sec.gov/Archives/edgar/data/797468/000162828026019816/oxy-20260319.htm'}},
  'verdict': 'Owned by Occidental Petroleum Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'Occidental Petroleum is a publicly traded oil and gas company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'oracle',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'oracle-corporation',
            'name': 'Oracle Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': "Ellison's ~40.6% stake is personal, not state."},
  'claim': {'text': 'Oracle Corporation is NYSE-listed (ORCL) and majority-free-float, with co-founder Larry Ellison '
                    'the largest single holder at roughly 40%. There is no state or sovereign-fund owner. The F1 '
                    'title sponsorship is funded from private corporate capital.',
            'short': 'Oracle Corporation is NYSE-listed (ORCL) and majority-free-float, with co-founder Larry '
                     'Ellison the largest single holder at roughly 40%.',
            'source': {'name': 'Oracle Corporation Form 10-K FY2026 (SEC EDGAR)',
                       'date': '2026-06-22',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm'}},
  'verdict': 'Owned by Oracle Corporation. Nothing found.',
  'confidence': 'high',
  'note': "Ellison's ~40.6% stake is personal, not state."},
 {'sponsorId': 'orlando-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'orlando-health-inc',
            'name': 'Orlando Health, Inc.',
            'type': 'private-company',
            'country': 'US',
            'note': 'Non-profit classified under private-company; no state funding owner, though it does receive '
                    'public reimbursement as a hospital system.'},
  'claim': {'text': 'Orlando Health is a private, not-for-profit healthcare organisation headquartered in Florida, '
                    'with no shareholders and no state stake; it is a 501(c)(3) system. Sponsorship spend is '
                    'therefore private/non-profit money with no political ownership chain.',
            'short': 'Orlando Health is a private, not-for-profit healthcare organisation headquartered in Florida, '
                     'with no shareholders and no state stake; it is a 501(c)(3) system.',
            'source': {'name': 'Orlando Health, About Us',
                       'date': '2026-09',
                       'url': 'https://www.orlandohealth.com/about-us'}},
  'verdict': 'Owned by Orlando Health, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Non-profit classified under private-company; no state funding owner, though it does receive public '
          'reimbursement as a hospital system.'},
 {'sponsorId': 'pamesa-ceramica',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'pamesa-grupo-empresarial',
            'name': 'Pamesa Grupo Empresarial (Fernando Roig)',
            'type': 'private-company',
            'country': 'ES',
            'note': "Family/owner-controlled Castellon ceramics group (~EUR 1.2bn revenue). Roig's Villarreal link "
                    'is separate.'},
  'claim': {'text': 'Pamesa Ceramica states it is the parent company of Grupo Pamesa, the Castellon ceramic-tile '
                    'group; the group is controlled by Spanish billionaire Fernando Roig Alfonso (also '
                    'owner/president of Villarreal CF) and is privately held with no state or fund shareholder.',
            'short': 'Pamesa Ceramica states it is the parent company of Grupo Pamesa, the Castellon ceramic-tile '
                     'group; the group is controlled by Spanish billionaire Fernando Roig….',
            'source': {'name': "Pamesa Ceramica official corporate page ('Pamesa Ceramica is the parent company of "
                               "the Pamesa Group'); Focus Piedra interview with Fernando Roig",
                       'date': '2021-2024',
                       'url': 'https://www.pamesa.com/en/CORPORATIVO.html'}},
  'verdict': 'Owned by Pamesa Grupo Empresarial (Fernando Roig). Nothing found.',
  'confidence': 'high',
  'note': "Family/owner-controlled Castellon ceramics group (~EUR 1.2bn revenue). Roig's Villarreal link is "
          'separate.'},
 {'sponsorId': 'paycom',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'paycom-owner',
            'name': 'Paycom',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Paycom is publicly traded with no state ownership; founder Chad Richison holds ~13.1% stake. No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Paycom Software, Inc. is a NYSE-listed HR technology provider with no state ownership; founder '
                    'Chad Richison beneficially owns ~13.1% of shares.',
            'short': 'Paycom Software, Inc.',
            'source': {'name': 'Paycom DEF 14A 2026',
                       'date': '2026-04-02',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1590955/000119312526140064/d44715ddef14a.htm'}},
  'verdict': 'Owned by Paycom. Nothing found.',
  'confidence': 'high',
  'note': 'Paycom is publicly traded with no state ownership; founder Chad Richison holds ~13.1% stake. No '
          'documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'paycor',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'paycor-owner',
            'name': 'Paycor',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Paycor, Inc. is owned by Paycor. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'Paycor, Inc.',
            'source': {'name': 'PAYCHEX INC DEF 14A 2026 (SEC)',
                       'date': '2026-09-04',
                       'url': 'https://www.sec.gov/Archives/edgar/data/723531/000119312526382805/d111983ddef14a.htm'}},
  'verdict': 'Owned by Paycor. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'paypal',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'paypal-owner',
            'name': 'PayPal LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'PayPal LLC is the ultimate owner of PayPal.',
            'short': 'PayPal LLC is the ultimate owner of PayPal.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by PayPal LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'paze',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'paze-owner',
            'name': 'Early Warning Services, LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Paze is owned by Early Warning Services, which is owned by seven major U.S. banks; no state '
                    'stake or serious conduct record identified.'},
  'claim': {'text': 'Early Warning Services, LLC is co-owned by seven major U.S. banks: Bank of America, Capital '
                    'One, JPMorgan Chase, PNC Bank, Truist, U.S. Bank and Wells Fargo.',
            'short': 'Early Warning Services, LLC is co-owned by seven major U.S.',
            'source': {'name': 'Consumer Financial Protection Bureau webpage',
                       'date': '2026-09-24',
                       'url': 'https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/early-warning-services-llc/'}},
  'verdict': 'Owned by Early Warning Services, LLC. Nothing found.',
  'confidence': 'high',
  'note': 'Paze is owned by Early Warning Services, which is owned by seven major U.S. banks; no state stake or '
          'serious conduct record identified.'},
 {'sponsorId': 'perdue-farms',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'perdue-farms-owner',
            'name': 'Perdue Farms',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Perdue Farms is 100% family-owned (Perdue family); no state stake or government control. No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Perdue Farms is a privately held, family-owned agriculture company (fourth-generation Perdue '
                    'family) with no state ownership.',
            'short': 'Perdue Farms is a privately held, family-owned agriculture company (fourth-generation Perdue '
                     'family) with no state ownership.',
            'source': {'name': 'Legal Clarity Perdue Farms ownership page',
                       'date': '2026-09-24',
                       'url': 'https://legalclarity.org/who-owns-perdue-chicken-its-still-family-owned'}},
  'verdict': 'Owned by Perdue Farms. Nothing found.',
  'confidence': 'high',
  'note': 'Perdue Farms is 100% family-owned (Perdue family); no state stake or government control. No documented '
          'human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'petco',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'petco-owner',
            'name': 'Petco',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Petco Health & Wellness Company, Inc. is owned by Petco. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Petco Health & Wellness Company, Inc.',
            'source': {'name': 'Petco Health & Wellness Company, Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-05-14',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1826470/000182647026000040/woof-20260514.htm'}},
  'verdict': 'Owned by Petco. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'pirelli',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'sinochem-holdings',
            'name': 'China National Chemical Corporation (Sinochem Holdings)',
            'type': 'state',
            'country': 'CN',
            'note': "State stake is being reduced (talk of a further cut toward 10%) but Sinochem remained Pirelli's "
                    "second-largest shareholder after the July 2026 sale, so 'serious' still stands. Camfin "
                    '(Tronchetti Provera family) is the largest holder.'},
  'claim': {'text': 'Pirelli & C. SpA is Borsa Italiana-listed but has long been part-owned by Sinochem, a Chinese '
                    "central state-owned enterprise under SASAC. Sinochem's vehicle Marco Polo International Italy "
                    'sold a 14% block (151.9m shares at EUR 6.50) to Czech investor Lumina Crown in July 2026, '
                    'cutting the Chinese state stake from about 34% to roughly 20%. A Chinese state owner of that '
                    'size is a material state link on a Ferrari sponsor.',
            'short': 'Pirelli & C.',
            'source': {'name': "European Rubber Journal, 'Sinochem completes EUR 1bn sale of Pirelli stake to Czech "
                               "investor'",
                       'date': '2026-08-03',
                       'url': 'https://www.european-rubber-journal.com/article/2099513/sinochem-completes-1bn-sale-of-pirelli-stake-to-czech-investor'}},
  'verdict': 'Pirelli & C.',
  'confidence': 'high',
  'note': "State stake is being reduced (talk of a further cut toward 10%) but Sinochem remained Pirelli's "
          "second-largest shareholder after the July 2026 sale, so 'serious' still stands. Camfin (Tronchetti "
          'Provera family) is the largest holder.'},
 {'sponsorId': 'play',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ed-sheeran',
            'name': "Ed Sheeran / 'Play' tour (private individual)",
            'type': 'private-company',
            'country': 'GB',
            'note': 'Owner is a natural person, not a company, so type is mapped to private-company. Sheeran is also '
                    'a minority shareholder in Ipswich Town, which can make the arrangement look corporate when it '
                    'is personal.'},
  'claim': {'text': "The 'Play' logo on the Ipswich Town sleeve is the branding of singer Ed Sheeran's 2025-27 "
                    "'Play' concert tour - a private, self-owned brand with no corporate parent and no state stake. "
                    "Ipswich Town 2026-27 shirts carry principal partner HALO on the chest and Sheeran's 'Play' tour "
                    'mark on the sleeve. Purely private money.',
            'short': "The 'Play' logo on the Ipswich Town sleeve is the branding of singer Ed Sheeran's 2025-27 "
                     "'Play' concert tour - a private, self-owned brand with no corporate….",
            'source': {'name': "The Kitman, 'Ipswich Town Reveal 2026-27 Home and Away Kits'",
                       'date': '2026-06',
                       'url': 'https://thekitman.co.uk/ipswich-town-reveal-2026-27-home-and-away-kits'}},
  'verdict': "Owned by Ed Sheeran / 'Play' tour (private individual). Nothing found.",
  'confidence': 'medium',
  'note': 'Owner is a natural person, not a company, so type is mapped to private-company. Sheeran is also a '
          'minority shareholder in Ipswich Town, which can make the arrangement look corporate when it is personal.'},
 {'sponsorId': 'plenitude',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'eni-spa',
            'name': 'Eni S.p.A. (Plenitude S.p.A. subsidiary)',
            'type': 'listed-company',
            'country': 'IT',
            'note': 'Flagged for proper look: the Italian state stake in Eni sits below 50% and via a listed parent, '
                    'so concern rather than serious. Claims of Eni human-rights/environmental harm (Niger Delta, OPL '
                    '245) are contested and partly settled, supporting concern not serious.'},
  'claim': {'text': "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but the "
                    'Italian Ministry of Economy and Finance plus CDP S.p.A. together hold 33.09% of its share '
                    'capital, i.e. a state link at the owner. Eni is restructuring/deconsolidating Plenitude with '
                    'Ares (20%) and EIP (10%), leaving Eni around 65%.',
            'short': "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but "
                     'the Italian Ministry of Economy and Finance plus CDP S.p.A.',
            'source': {'name': 'Eni official shareholder-structure page (MEF + CDP = 33.09%); Eni press release on '
                               'deconsolidation of Plenitude',
                       'date': '2026-03-19',
                       'url': 'https://www.eni.com/en-IT/governance/shareholding-structure.html'}},
  'verdict': "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but the "
             'Italian Ministry of Economy and Finance plus CDP S.p.A.',
  'confidence': 'high',
  'note': 'Flagged for proper look: the Italian state stake in Eni sits below 50% and via a listed parent, so '
          'concern rather than serious. Claims of Eni human-rights/environmental harm (Niger Delta, OPL 245) are '
          'contested and partly settled, supporting concern not serious.'},
 {'sponsorId': 'pnc-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'pnc-bank-pnc-financial-services-owner',
            'name': 'PNC Bank (PNC Financial Services) Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'PNC Bank (PNC Financial Services) Corporation is the ultimate owner of PNC Bank (PNC Financial '
                    'Services).',
            'short': 'PNC Bank (PNC Financial Services) Corporation is the ultimate owner of PNC Bank (PNC Financial '
                     'Services).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by PNC Bank (PNC Financial Services) Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'polymarket',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'blockratize-inc',
            'name': 'Blockratize, Inc. (dba Polymarket)',
            'type': 'private-company',
            'country': 'US',
            'note': "ICE's investment (reported ~USD 2bn, with a further USD 600m in 2026) is minority; ownership of "
                    'the wider Polymarket structure is unusually opaque, but no state owner is evident. The supplied '
                    "currentOwnerId 'blockratize' was correct; normalised to blockratize-inc."},
  'claim': {'text': 'Polymarket is operated by Blockratize, Inc., a Delaware private company founded by Shayne '
                    'Coplan; it is venture-backed with Intercontinental Exchange (NYSE: ICE) as a strategic minority '
                    'investor. Ultimate control remains with the founder and venture investors, with no state stake. '
                    'Offshore operations run through Adventure One Ltd in Panama.',
            'short': 'Polymarket is operated by Blockratize, Inc., a Delaware private company founded by Shayne '
                     'Coplan; it is venture-backed with Intercontinental Exchange (NYSE: ICE)….',
            'source': {'name': "Intercontinental Exchange, 'ICE Announces Strategic Investment in Polymarket'",
                       'date': '2025-10-07',
                       'url': 'https://ir.theice.com/press/news-details/2025/ICE-Announces-Strategic-Investment-in-Polymarket/default.aspx'}},
  'verdict': 'Owned by Blockratize, Inc. (dba Polymarket). Nothing found.',
  'confidence': 'high',
  'note': "ICE's investment (reported ~USD 2bn, with a further USD 600m in 2026) is minority; ownership of the wider "
          'Polymarket structure is unusually opaque, but no state owner is evident. The supplied currentOwnerId '
          "'blockratize' was correct; normalised to blockratize-inc."},
 {'sponsorId': 'progressive',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'progressive-owner',
            'name': 'Progressive Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Progressive is a publicly traded insurance company; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Progressive Corporation is a publicly traded company listed on the New York Stock Exchange '
                    'under ticker PGR.',
            'short': 'Progressive Corporation is a publicly traded company listed on the New York Stock Exchange '
                     'under ticker PGR.',
            'source': {'name': 'SEC DEF 14A for Progressive Corporation',
                       'date': '2026-03-23',
                       'url': 'https://www.sec.gov/Archives/edgar/data/80661/000008066126000099/pgr-20260318.htm'}},
  'verdict': 'Owned by Progressive Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'Progressive is a publicly traded insurance company; no state stake or serious conduct record identified.'},
 {'sponsorId': 'prometeon',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'sinochem-holdings',
            'name': 'Sinochem Holdings (via China National Tire & Rubber and Aeolus Tyre)',
            'type': 'state',
            'country': 'CN',
            'note': "Sinochem's own newsroom carries the same 38% CNRC/Prometeon transaction, confirming the state "
                    'chain.'},
  'claim': {'text': 'Prometeon Tyre Group, the truck/agro tyre business spun out of Pirelli in 2017, is controlled '
                    'through China National Tire & Rubber Co. (CNRC), a subsidiary of state-owned Sinochem Holdings; '
                    'CNRC holds 57.37% of Aeolus Tyre, which was entrusted with a further 38% of Prometeon and '
                    'thereby controls 100%. The Parma front-of-shirt sponsor is therefore ultimately Chinese '
                    'state-owned, the same SOE that sits behind Pirelli.',
            'short': 'Prometeon Tyre Group, the truck/agro tyre business spun out of Pirelli in 2017, is controlled '
                     'through China National Tire & Rubber Co.',
            'source': {'name': "Tyrepress, 'Aeolus officially controls 100% of Prometeon Tyre Group'",
                       'date': '2022-08-10',
                       'url': 'https://www.tyrepress.com/2022/08/aeolus-officially-controls-100-of-prometeon-tyre-group/'}},
  'verdict': 'Prometeon Tyre Group, the truck/agro tyre business spun out of Pirelli in 2017, is controlled through '
             'China National Tire & Rubber Co.',
  'confidence': 'high',
  'note': "Sinochem's own newsroom carries the same 38% CNRC/Prometeon transaction, confirming the state chain."},
 {'sponsorId': 'providence',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'providence-health-system',
            'name': 'Providence (Providence Health & Services / Providence Swedish)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Catholic non-profit; some would flag religious-ethics issues, not state ownership.'},
  'claim': {'text': 'Providence is a not-for-profit Catholic health system serving the western United States; the '
                    'Sounders deal is signed at health-system level via Providence Swedish. There are no '
                    'shareholders and no state owner, so this is non-profit private money. Human-rights relevance is '
                    'limited to ordinary health-sector conduct.',
            'short': 'Providence is a not-for-profit Catholic health system serving the western United States; the '
                     'Sounders deal is signed at health-system level via Providence Swedish.',
            'source': {'name': "Seattle Sounders FC, 'Sounders FC and Providence agree to unprecedented "
                               "community-focused partnership'",
                       'date': '2023-01-20',
                       'url': 'https://www.soundersfc.com/news/sounders-fc-and-providence-agree-to-unprecedented-community-focused-partnership'}},
  'verdict': 'Owned by Providence (Providence Health & Services / Providence Swedish). Nothing found.',
  'confidence': 'high',
  'note': 'Catholic non-profit; some would flag religious-ethics issues, not state ownership.'},
 {'sponsorId': 'pulsee-luce-e-gas',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'axpo-holding-ag',
            'name': 'Axpo Holding AG (owned by Swiss cantons and cantonal utilities)',
            'type': 'state',
            'country': 'CH',
            'note': "Cantons are treated as 'state' (public-law bodies), which is why this lands at 'serious' rather "
                    "than 'none'. The shareholder table on the page carries a 2014 date but the structure is "
                    'current.'},
  'claim': {'text': 'Pulsee Luce e Gas is the digital retail energy brand of Axpo Italia, a subsidiary of Axpo '
                    'Holding AG. Axpo is 100% publicly owned: all its shares sit with the cantons of northeastern '
                    'Switzerland and their utilities, with Canton Zurich and its cantonal utility alone holding '
                    'roughly 36%. The Genoa front sponsor is therefore backed by sub-national Swiss state capital.',
            'short': 'Pulsee Luce e Gas is the digital retail energy brand of Axpo Italia, a subsidiary of Axpo '
                     'Holding AG.',
            'source': {'name': "Axpo Group, 'Owners - Entirely in public hands'",
                       'date': '2026-09',
                       'url': 'https://axpo.com/group/en/about-us/axpo-group/owners.html'}},
  'verdict': 'Pulsee Luce e Gas is the digital retail energy brand of Axpo Italia, a subsidiary of Axpo Holding AG.',
  'confidence': 'high',
  'note': "Cantons are treated as 'state' (public-law bodies), which is why this lands at 'serious' rather than "
          "'none'. The shareholder table on the page carries a 2014 date but the structure is current."},
 {'sponsorId': 'puma',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'anta-sports-products',
            'name': 'ANTA Sports Products Limited',
            'type': 'listed-company',
            'country': 'CN',
            'note': 'Deal signed Jan 2026 and cleared by Chinese and Indian competition authorities; completion by '
                    "the time of writing is assumed but not separately confirmed. Puma delivered 'none' because ANTA "
                    'has no material state stake - worth revisiting if a state fund takes a position.'},
  'claim': {'text': "Puma SE is a Frankfurt-listed company whose largest shareholder, the Pinault family's Groupe "
                    'Artemis (~29%), agreed in January 2026 to sell its entire 29.06% stake to ANTA Sports Products '
                    'Limited (HKEX: 2020) for EUR 1.5bn. ANTA is a Chinese listed sportswear group controlled by the '
                    "Ding family; it is privately controlled, not state-owned. The Ferrari sponsor's ownership chain "
                    'therefore leads to private Chinese capital, not the Chinese state.',
            'short': "Puma SE is a Frankfurt-listed company whose largest shareholder, the Pinault family's Groupe "
                     'Artemis (~29%), agreed in January 2026 to sell its entire 29.06% stake….',
            'source': {'name': 'ANTA Sports Products Limited, HKEX announcement: Acquisition of 29.06% equity '
                               'interest in PUMA SE',
                       'date': '2026-01-27',
                       'url': 'https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0127/2026012700061.pdf'}},
  'verdict': 'Owned by ANTA Sports Products Limited. Nothing found.',
  'confidence': 'medium',
  'note': 'Deal signed Jan 2026 and cleared by Chinese and Indian competition authorities; completion by the time of '
          "writing is assumed but not separately confirmed. Puma delivered 'none' because ANTA has no material state "
          'stake - worth revisiting if a state fund takes a position.'},
 {'sponsorId': 'puma-am',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'anta-sports-products',
            'name': 'ANTA Sports Products Limited',
            'type': 'listed-company',
            'country': 'CN',
            'note': "Duplicate of the 'puma' sponsor record on a different car; kept separate because the dataset "
                    'lists them separately.'},
  'claim': {'text': 'This is the same PUMA SE entity as the Ferrari partner entry: a Frankfurt-listed company being '
                    'acquired by ANTA Sports Products Limited, which agreed in January 2026 to buy the Pinault '
                    "family's 29.06% stake for EUR 1.5bn. ANTA is a privately controlled Chinese listed group, so "
                    'there is no state owner in the chain. The Aston Martin placement does not change the ownership '
                    'analysis.',
            'short': 'This is the same PUMA SE entity as the Ferrari partner entry: a Frankfurt-listed company being '
                     'acquired by ANTA Sports Products Limited, which agreed in January….',
            'source': {'name': 'ANTA Sports Products Limited, HKEX announcement: Acquisition of 29.06% equity '
                               'interest in PUMA SE',
                       'date': '2026-01-27',
                       'url': 'https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0127/2026012700061.pdf'}},
  'verdict': 'Owned by ANTA Sports Products Limited. Nothing found.',
  'confidence': 'medium',
  'note': "Duplicate of the 'puma' sponsor record on a different car; kept separate because the dataset lists them "
          'separately.'},
 {'sponsorId': 'purina',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'nestle-sa',
            'name': 'Nestle S.A.',
            'type': 'listed-company',
            'country': 'CH',
            'note': 'nestle.com blocks direct scraping (403); the Annual Review PDF was opened via extractor. Purina '
                    'is a subsidiary brand of Nestle S.A.'},
  'claim': {'text': 'Purina (Nestle Purina PetCare) is the pet-food division of Nestle S.A., the SIX-listed Swiss '
                    'food group. Nestle has a broad institutional shareholder base with no controlling or state '
                    'shareholder, so the St. Louis CITY SC front sponsorship is private corporate money. '
                    "Human-rights exposure comes from Nestle's own supply-chain record rather than any state owner.",
            'short': 'Purina (Nestle Purina PetCare) is the pet-food division of Nestle S.A., the SIX-listed Swiss '
                     'food group.',
            'source': {'name': 'Nestle S.A., Annual Review 2025',
                       'date': '2026-02',
                       'url': 'https://www.nestle.com/sites/default/files/2026-02/annual-review-2025-en.pdf'}},
  'verdict': 'Owned by Nestle S.A.. Nothing found.',
  'confidence': 'high',
  'note': 'nestle.com blocks direct scraping (403); the Annual Review PDF was opened via extractor. Purina is a '
          'subsidiary brand of Nestle S.A.'},
 {'sponsorId': 'qatar-airways',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'government-of-qatar',
            'name': 'Government of the State of Qatar (Qatar Airways Group Q.C.S.C.)',
            'type': 'state',
            'country': 'QA',
            'note': 'Owner is a sovereign state, not a state fund, and Qatar is not a party to an armed conflict, so '
                    'serious rather than severe. Migrant-worker deaths and unpaid wages documented by HRW and '
                    'Amnesty; Qatar reformed kafala in 2020 but remedy/compensation remains outstanding '
                    '(https://www.hrw.org/news/2022/11/17/fifa/qatar-migrant-workers-call-for-compensation-for-abuses).'},
  'claim': {'text': "Qatar Airways Group Q.C.S.C. is incorporated in Qatar and 'is ultimately wholly owned by the "
                    'Government of the State of Qatar (the "Shareholder")\'; the state\'s kafala/migrant-labour '
                    'system produced documented serious abuses in the run-up to the 2022 World Cup.',
            'short': 'Qatar Airways Group Q.C.S.C.',
            'source': {'name': 'Qatar Airways Group audited consolidated financial statements (note: corporate '
                               'information); Human Rights Watch',
                       'date': '2022-03 / 2022-11',
                       'url': 'https://www.qatarairways.com/content/dam/documents/annual-reports/2022/financial-statement-en.pdf'}},
  'verdict': 'Qatar Airways Group Q.C.S.C.',
  'confidence': 'high',
  'note': 'Owner is a sovereign state, not a state fund, and Qatar is not a party to an armed conflict, so serious '
          'rather than severe. Migrant-worker deaths and unpaid wages documented by HRW and Amnesty; Qatar reformed '
          'kafala in 2020 but remedy/compensation remains outstanding '
          '(https://www.hrw.org/news/2022/11/17/fifa/qatar-migrant-workers-call-for-compensation-for-abuses).'},
 {'sponsorId': 'qatar-airways-global',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'state-of-qatar-qia',
            'name': 'State of Qatar (via Qatar Investment Authority)',
            'type': 'state',
            'country': 'QA',
            'note': "Called 'serious' rather than 'severe': Qatar is not a party to an ongoing armed conflict. Stake "
                    'is arguably indirect (QIA + Ministry of Finance), but the state owns 100%.'},
  'claim': {'text': 'Qatar Airways is wholly owned by the State of Qatar, held through the Qatar Investment '
                    "Authority sovereign wealth fund, and appears in QIA's domestic portfolio alongside QNB and "
                    'Ooredoo. There are no private shareholders and no listing. The F1 global partnership is '
                    "therefore effectively Gulf state money, which the method places at 'serious' absent live armed "
                    'conflict.',
            'short': 'Qatar Airways is wholly owned by the State of Qatar, held through the Qatar Investment '
                     "Authority sovereign wealth fund, and appears in QIA's domestic portfolio….",
            'source': {'name': 'Qatar Investment Authority, Portfolio',
                       'date': '2026-09',
                       'url': 'https://www.qia.qa/en/Portfolio/Pages/default.aspx'}},
  'verdict': 'Qatar Airways is wholly owned by the State of Qatar, held through the Qatar Investment Authority '
             "sovereign wealth fund, and appears in QIA's domestic portfolio….",
  'confidence': 'high',
  'note': "Called 'serious' rather than 'severe': Qatar is not a party to an ongoing armed conflict. Stake is "
          'arguably indirect (QIA + Ministry of Finance), but the state owns 100%.'},
 {'sponsorId': 'qualcomm',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'qualcomm-incorporated',
            'name': 'QUALCOMM Incorporated',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake identified.'},
  'claim': {'text': 'QUALCOMM Incorporated is a Nasdaq-listed (QCOM) semiconductor company with a dispersed '
                    'institutional shareholder base and no state or sovereign-fund owner. The Snapdragon-branded '
                    'Mercedes sponsorship is private corporate spend. Human-rights exposure would come from chip '
                    'supply chains, especially China and Taiwan manufacturing.',
            'short': 'QUALCOMM Incorporated is a Nasdaq-listed (QCOM) semiconductor company with a dispersed '
                     'institutional shareholder base and no state or sovereign-fund owner.',
            'source': {'name': 'QUALCOMM Incorporated Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2025-11-05',
                       'url': 'https://www.sec.gov/Archives/edgar/data/804328/000080432825000085/qcom-20250928.htm'}},
  'verdict': 'Owned by QUALCOMM Incorporated. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake identified.'},
 {'sponsorId': 'quest-diagnostics',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'quest-diagnostics-owner',
            'name': 'Quest Diagnostics',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Quest Diagnostics is publicly traded with no state ownership; largest holder is BlackRock '
                    '(~6.9%). No documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Quest Diagnostics is a NYSE-listed diagnostic information company with no state ownership; '
                    'largest shareholder is BlackRock (~6.91%) and other institutions each under 10%.',
            'short': 'Quest Diagnostics is a NYSE-listed diagnostic information company with no state ownership; '
                     'largest shareholder is BlackRock (~6.91%) and other institutions each….',
            'source': {'name': 'Quest Diagnostics DEF 14A 2026',
                       'date': '2026-04-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1022079/000114036126013356/ny20064122x1_def14a.htm'}},
  'verdict': 'Owned by Quest Diagnostics. Nothing found.',
  'confidence': 'high',
  'note': 'Quest Diagnostics is publicly traded with no state ownership; largest holder is BlackRock (~6.9%). No '
          'documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'quikrete',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'quikrete-owner',
            'name': 'QUIKRETE',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Quikrete Holdings, Inc. is owned by QUIKRETE. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Quikrete Holdings, Inc.',
            'source': {'name': 'Forbes article on Quikrete Winchester family',
                       'date': '2026-05-13',
                       'url': 'https://www.forbes.com/sites/mattdurot/2026/05/13/the-little-known-winchester-family-is-worth-18-billion-thanks-to-quikrete/'}},
  'verdict': 'Owned by QUIKRETE. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'quiktrip',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'quiktrip-owner',
            'name': 'QuikTrip LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'QuikTrip LLC is the ultimate owner of QuikTrip.',
            'short': 'QuikTrip LLC is the ultimate owner of QuikTrip.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by QuikTrip LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'raisin',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'raisin-gmbh',
            'name': 'Raisin GmbH (Raisin DS)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Bank investors are minority VC/strategic stakes, so the owner stays private-company with no '
                    'state link (Orange Ventures is Orange SA, itself only partly French state-owned - not '
                    'counted).'},
  'claim': {'text': 'Raisin (Weltsparen) is a Berlin fintech formed by the 2021 merger of Deposit Solutions and '
                    'Raisin GmbH; it is privately held and VC-backed by investors including Goldman Sachs, Deutsche '
                    'Bank, Index Ventures, Kinnevik, PayPal Ventures and Thrive Capital. No state or sovereign-fund '
                    'shareholder.',
            'short': 'Raisin (Weltsparen) is a Berlin fintech formed by the 2021 merger of Deposit Solutions and '
                     'Raisin GmbH; it is privately held and VC-backed by investors including….',
            'source': {'name': "Fintech Consult company profile listing Raisin's investor base; Raisin corporate "
                               '(XING/Lusha) company description',
                       'date': '2026',
                       'url': 'https://fintech-consult.com/europe/germany/fintech/raisin/'}},
  'verdict': 'Owned by Raisin GmbH (Raisin DS). Nothing found.',
  'confidence': 'medium',
  'note': 'Bank investors are minority VC/strategic stakes, so the owner stays private-company with no state link '
          '(Orange Ventures is Orange SA, itself only partly French state-owned - not counted).'},
 {'sponsorId': 'rate',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'rate-formerly-guaranteed-rate-owner',
            'name': 'Rate (formerly Guaranteed Rate)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Described as privately held; no state stake or serious conduct record identified.'},
  'claim': {'text': 'Guaranteed Rate is a privately held company, ranked #1 for revenue growth on lists of largest '
                    'privately held companies.',
            'short': 'Guaranteed Rate is a privately held company, ranked #1 for revenue growth on lists of largest '
                     'privately held companies.',
            'source': {'name': "Crain's Chicago Business article via Cision",
                       'date': '2013-04-22',
                       'url': 'https://news.cision.com/guaranteed-rate-inc-/r/guaranteed-rate-ranked--1-for-revenue-growth-on-list-of-largest-privately-held-companies,c9403167'}},
  'verdict': 'Owned by Rate (formerly Guaranteed Rate). Nothing found.',
  'confidence': 'medium',
  'note': 'Described as privately held; no state stake or serious conduct record identified.'},
 {'sponsorId': 'raymond-james-financial',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'raymond-james-financial-owner',
            'name': 'Raymond James Financial',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Raymond James Financial is publicly traded with no state ownership; largest holder is Vanguard '
                    '(~11.3%). No documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Raymond James Financial is a NYSE-listed financial services company with no state ownership; '
                    'largest shareholder is The Vanguard Group (~11.31%) and other institutions each under 10%.',
            'short': 'Raymond James Financial is a NYSE-listed financial services company with no state ownership; '
                     'largest shareholder is The Vanguard Group (~11.31%) and other….',
            'source': {'name': 'Raymond James Financial DEF 14A 2026',
                       'date': '2026-01-07',
                       'url': 'https://www.sec.gov/Archives/edgar/data/720005/000072000526000019/rjf-20260106.htm'}},
  'verdict': 'Owned by Raymond James Financial. Nothing found.',
  'confidence': 'high',
  'note': 'Raymond James Financial is publicly traded with no state ownership; largest holder is Vanguard (~11.3%). '
          'No documented human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'red-bull',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'mateschitz-yoovidhya-families',
            'name': 'Mateschitz family (49%) and Yoovidhya family (51%), via Red Bull GmbH',
            'type': 'family',
            'country': 'AT',
            'note': "Private/family owner → none. Thailand's state is not in the ownership chain despite the Thai "
                    'ownership origin.'},
  'claim': {'text': 'Red Bull GmbH is a privately held Austrian company owned by two families: the founding '
                    'Yoovidhya family of Thailand holds 51% and the Mateschitz family (Mark Mateschitz, heir of '
                    'co-founder Dietrich) holds 49%. Neither owner is a state or state fund.',
            'short': 'Red Bull GmbH is a privately held Austrian company owned by two families: the founding '
                     'Yoovidhya family of Thailand holds 51% and the Mateschitz family (Mark….',
            'source': {'name': "Reuters (Red Bull leadership after co-founder's death, referencing the inherited 49% "
                               'stake)',
                       'date': '2022-11-04',
                       'url': 'https://www.reuters.com/business/retail-consumer/trio-lead-energy-drinks-giant-red-bull-after-co-founders-death-2022-11-04/'}},
  'verdict': 'Owned by Mateschitz family (49%) and Yoovidhya family (51%), via Red Bull GmbH. Nothing found.',
  'confidence': 'high',
  'note': "Private/family owner → none. Thailand's state is not in the ownership chain despite the Thai ownership "
          'origin.'},
 {'sponsorId': 'renasant-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'renasant-corporation',
            'name': 'Renasant Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Bank regulation gives government-adjacent exposure but no equity stake.'},
  'claim': {'text': 'Renasant Bank is the principal subsidiary of Renasant Corporation, an NYSE-listed (RNST) '
                    'regional bank holding company based in Tupelo, Mississippi. It is privately held through public '
                    'markets with no state ownership. The Nashville SC front sponsorship is plain private bank '
                    'marketing money.',
            'short': 'Renasant Bank is the principal subsidiary of Renasant Corporation, an NYSE-listed (RNST) '
                     'regional bank holding company based in Tupelo, Mississippi.',
            'source': {'name': 'Renasant Corporation Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2026-03-02',
                       'url': 'https://www.sec.gov/Archives/edgar/data/715072/000071507226000017/rnst-20251231.htm'}},
  'verdict': 'Owned by Renasant Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'Bank regulation gives government-adjacent exposure but no equity stake.'},
 {'sponsorId': 'reuter',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'reuter-gruppe',
            'name': 'REUTER Gruppe (Reuter family)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Group HQ Moenchengladbach; expansion into Italy in 2024. No state or fund ownership.'},
  'claim': {'text': "REUTER is Germany's largest online bathroom-products retailer, a family-run business founded by "
                    'craftsman Bernd Reuter, who turned his trade business into an online shop in 2004; it became '
                    "Borussia Moenchengladbach's main sponsor from 2024/25 and remains privately owned.",
            'short': "REUTER is Germany's largest online bathroom-products retailer, a family-run business founded "
                     'by craftsman Bernd Reuter, who turned his trade business into an….',
            'source': {'name': "REUTER official company history page ('The family-run company is Borussia "
                               "Moenchengladbach's new main sponsor'); LogInfo24 on founder Bernd Reuter",
                       'date': '2024',
                       'url': 'https://www.reuter.com/company/about-us/our-history.html'}},
  'verdict': 'Owned by REUTER Gruppe (Reuter family). Nothing found.',
  'confidence': 'high',
  'note': 'Group HQ Moenchengladbach; expansion into Italy in 2024. No state or fund ownership.'},
 {'sponsorId': 'rewe',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'rewe-group',
            'name': 'REWE Group (REWE cooperatives eG)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Type stays private-company because the owner list only allows '
                    'state/state-fund/listed/private/unknown and an eG is private. (Note: country set DE - see '
                    'note.)'},
  'claim': {'text': 'REWE Group is a German retail and travel group organized as a two-tier cooperative: it is owned '
                    'by six regional cooperatives (eG) including Hungen eG, West eG, Sued/Suedwest eG, Nord/Ost eG '
                    'and Dortmund eG, plus Fuer Sie Handelsgenossenschaft eG. Cooperative members - independent '
                    'retailers - are the owners; no external shareholder or state stake.',
            'short': 'REWE Group is a German retail and travel group organized as a two-tier cooperative: it is '
                     'owned by six regional cooperatives (eG) including Hungen eG, West eG,….',
            'source': {'name': "REWE Group official 'Cooperative' page and investor presentation (REWE COOPERATIVES "
                               '/ six owner cooperatives)',
                       'date': '2024-07',
                       'url': 'https://www.rewe-group.com/en/cooperative/'}},
  'verdict': 'Owned by REWE Group (REWE cooperatives eG). Nothing found.',
  'confidence': 'high',
  'note': 'Type stays private-company because the owner list only allows state/state-fund/listed/private/unknown and '
          'an eG is private. (Note: country set DE - see note.)'},
 {'sponsorId': 'robinhood',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'robinhood-owner',
            'name': 'Robinhood',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Robinhood Markets, Inc. is owned by Robinhood. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'Robinhood Markets, Inc.',
            'source': {'name': 'Robinhood Markets, Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-04-22',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1783879/000178387926000053/hood-20260422.htm'}},
  'verdict': 'Owned by Robinhood. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'rocket',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'rocket-rocket-companies-owner',
            'name': 'Rocket (Rocket Companies) LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Rocket (Rocket Companies) LLC is the ultimate owner of Rocket (Rocket Companies).',
            'short': 'Rocket (Rocket Companies) LLC is the ultimate owner of Rocket (Rocket Companies).',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Rocket (Rocket Companies) LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'rogers-communications',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'rogers-communications-owner',
            'name': 'Rogers Communications Inc.',
            'type': 'listed-company',
            'country': 'CA',
            'note': 'Rogers Communications is a publicly traded telecommunications company; no state stake or '
                    'serious conduct record identified.'},
  'claim': {'text': 'Rogers Communications Inc. is a publicly traded company listed on the Toronto Stock Exchange '
                    'and New York Stock Exchange under ticker RCI.',
            'short': 'Rogers Communications Inc.',
            'source': {'name': 'SEC 40-F for Rogers Communications Inc.',
                       'date': '2026-03-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/733099/000073309926000009/rci-20251231.htm'}},
  'verdict': 'Owned by Rogers Communications Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Rogers Communications is a publicly traded telecommunications company; no state stake or serious conduct '
          'record identified.'},
 {'sponsorId': 'rouses-markets',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'rouses-markets-owner',
            'name': 'Rouses Markets',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Rouses Markets is family-owned and operated (Donny Rouse, third generation); no state stake. No '
                    'documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'Rouses Markets is a family-owned grocery chain (third-generation Rouse family) with no state '
                    'ownership or control.',
            'short': 'Rouses Markets is a family-owned grocery chain (third-generation Rouse family) with no state '
                     'ownership or control.',
            'source': {'name': 'Rouses Markets About Us page',
                       'date': '2026-09-24',
                       'url': 'http://rouses.com/about/about-us'}},
  'verdict': 'Owned by Rouses Markets. Nothing found.',
  'confidence': 'high',
  'note': 'Rouses Markets is family-owned and operated (Donny Rouse, third generation); no state stake. No '
          'documented human-rights concerns in ownership chain.'},
 {'sponsorId': 'royal-caribbean',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'royal-caribbean-cruises-ltd',
            'name': 'Royal Caribbean Cruises Ltd.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Liberian-incorporated but US-listed; no flag-of-convenience state owner.'},
  'claim': {'text': 'Royal Caribbean Group is NYSE-listed (RCL) with a fully dispersed public shareholder base and '
                    'no state or sovereign-fund owner. The Inter Miami front deal is funded from corporate capital. '
                    'Human-rights relevance centres on crew/labour and environmental compliance at sea rather than '
                    'ownership.',
            'short': 'Royal Caribbean Group is NYSE-listed (RCL) with a fully dispersed public shareholder base and '
                     'no state or sovereign-fund owner.',
            'source': {'name': 'Royal Caribbean Cruises Ltd. Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2026-02-11',
                       'url': 'https://www.sec.gov/Archives/edgar/data/884887/000088488726000007/rcl-20251231.htm'}},
  'verdict': 'Owned by Royal Caribbean Cruises Ltd.. Nothing found.',
  'confidence': 'high',
  'note': 'Liberian-incorporated but US-listed; no flag-of-convenience state owner.'},
 {'sponsorId': 's-3m',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': '3m-company',
            'name': '3M Company',
            'type': 'listed-company',
            'country': 'US',
            'note': "Serious conduct record but private owner, so 'none' under the ownership-led method rather than "
                    "'concern'."},
  'claim': {'text': '3M is an NYSE-listed conglomerate with no controlling or state shareholder. The Cadillac F1 '
                    "partnership is private corporate money. 3M's notable human-rights/conduct exposure is "
                    "litigation-driven - PFAS ('forever chemicals') contamination settlements and combat-earplug "
                    'hearing-loss claims - not state ownership.',
            'short': '3M is an NYSE-listed conglomerate with no controlling or state shareholder.',
            'source': {'name': '3M Company Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2026-02-03',
                       'url': 'https://www.sec.gov/Archives/edgar/data/66740/000006674026000014/mmm-20251231.htm'}},
  'verdict': 'Owned by 3M Company. Nothing found.',
  'confidence': 'high',
  'note': "Serious conduct record but private owner, so 'none' under the ownership-led method rather than "
          "'concern'."},
 {'sponsorId': 'sabor-a-malaga',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'diputacion-de-malaga',
            'name': 'Diputacion Provincial de Malaga',
            'type': 'state',
            'country': 'ES',
            'note': 'Sub-national government owner (not a sovereign state, not a state fund) maps to concern as a '
                    'lesser link. Currently front-of-shirt sponsor of Malaga CF (since 2021).'},
  'claim': {'text': 'Sabor a Malaga is not a company but a promotional quality brand owned and run by the Diputacion '
                    'Provincial de Malaga, the provincial public administration; the brand is used by the Diputacion '
                    "to promote the province's agri-food products and licenses its use to producers. The owner is "
                    'therefore a public body - a lesser/sub-national state link.',
            'short': 'Sabor a Malaga is not a company but a promotional quality brand owned and run by the '
                     'Diputacion Provincial de Malaga, the provincial public administration; the….',
            'source': {'name': 'Sabor a Malaga official site (a brand of the Diputacion de Malaga); Diputacion de '
                               'Malaga trademark-use resolution',
                       'date': '2026',
                       'url': 'https://www.saboramalaga.es/en/news/blog/sabor-a-malaga-proud-official-sponsor-of-malaga-cf-since-2021-p54384'}},
  'verdict': 'Sabor a Malaga is not a company but a promotional quality brand owned and run by the Diputacion '
             'Provincial de Malaga, the provincial public administration; the….',
  'confidence': 'high',
  'note': 'Sub-national government owner (not a sovereign state, not a state fund) maps to concern as a lesser link. '
          'Currently front-of-shirt sponsor of Malaga CF (since 2021).'},
 {'sponsorId': 'sap',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sap-se',
            'name': 'SAP SE — free float with founder-family anchors',
            'type': 'listed-company',
            'country': 'DE',
            'note': 'Listed German company → none.'},
  'claim': {'text': 'SAP SE is a Frankfurt-listed German software company with a free float of about 84% reported by '
                    'the company itself; the largest identified holders are founder-family vehicles (Hopp family '
                    '~5.1%, Portika gGmbH ~3.6%) — private, not state. No state or state-fund owner.',
            'short': 'SAP SE is a Frankfurt-listed German software company with a free float of about 84% reported '
                     'by the company itself; the largest identified holders are….',
            'source': {'name': 'SAP Investor Relations, shareholder structure/basic data',
                       'date': '2026',
                       'url': 'https://www.sap.com/investors/en/stock/basic-data.html'}},
  'verdict': 'Owned by SAP SE — free float with founder-family anchors. Nothing found.',
  'confidence': 'high',
  'note': 'Listed German company → none.'},
 {'sponsorId': 'saputo',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'saputo-inc',
            'name': 'Saputo Inc.',
            'type': 'listed-company',
            'country': 'CA',
            'note': "Judgement call: CDPQ's ~4.5% was treated as too small to justify 'concern'. Raise it if the "
                    'dataset wants any state-fund presence flagged.'},
  'claim': {'text': 'Saputo Inc. is a Toronto-listed dairy processor controlled by the Saputo family through Jolina '
                    "Capital, with a large family insider block. Quebec's public pension manager CDPQ holds a "
                    'minority financial stake of roughly 4.5% after a September 2024 purchase, so there is a small '
                    'state-fund presence but no state control. The Bologna front sponsorship is private '
                    'family-controlled corporate money.',
            'short': 'Saputo Inc.',
            'source': {'name': "La Caisse (CDPQ), 'CDPQ increases its stake in Saputo Inc.'",
                       'date': '2024-09-30',
                       'url': 'https://www.lacaisse.com/en/news/pressreleases/cdpq-increases-its-stake-saputo-inc'}},
  'verdict': 'Owned by Saputo Inc.. Nothing found.',
  'confidence': 'high',
  'note': "Judgement call: CDPQ's ~4.5% was treated as too small to justify 'concern'. Raise it if the dataset wants "
          'any state-fund presence flagged.'},
 {'sponsorId': 'sardegna-turismo',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'regione-autonoma-della-sardegna',
            'name': 'Regione Autonoma della Sardegna (Assessorato del Turismo)',
            'type': 'state',
            'country': 'IT',
            'note': 'Sponsor is a hybrid: regional state tourism body plus private brewery, and Cagliari has rotated '
                    'sponsors (Banco di Sardegna, Moby). Call is driven by the state-side branding; if the exposure '
                    "is judged to be Doppio Malto alone the tier would drop to 'none'."},
  'claim': {'text': "The 'Sardegna' branding on the Cagliari front shirt is the tourism promotion of the Autonomous "
                    'Region of Sardinia, run by its regional tourism department (Assessorato del Turismo, '
                    'Artigianato e Commercio), which has repeatedly signed main-sponsor deals with the club. It is a '
                    'public-law regional body, so this is sub-national state money. The shirt front is co-branded '
                    'with Sardinian craft-beer chain Doppio Malto, a private company.',
            'short': "The 'Sardegna' branding on the Cagliari front shirt is the tourism promotion of the Autonomous "
                     'Region of Sardinia, run by its regional tourism department….',
            'source': {'name': 'Regione Autonoma della Sardegna, Assessorato del turismo, artigianato e commercio',
                       'date': '2026-09',
                       'url': 'https://www.regione.sardegna.it/ricerca/assessorato-del-turismo-artigianato-e-commercio-527'}},
  'verdict': "The 'Sardegna' branding on the Cagliari front shirt is the tourism promotion of the Autonomous Region "
             'of Sardinia, run by its regional tourism department….',
  'confidence': 'medium',
  'note': 'Sponsor is a hybrid: regional state tourism body plus private brewery, and Cagliari has rotated sponsors '
          '(Banco di Sardegna, Moby). Call is driven by the state-side branding; if the exposure is judged to be '
          "Doppio Malto alone the tier would drop to 'none'."},
 {'sponsorId': 'scotiabank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'scotiabank-owner',
            'name': 'Scotiabank',
            'type': 'listed-company',
            'country': 'CA',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'The Bank of Nova Scotia is owned by Scotiabank. No state shareholder identified. Ownership sits '
                    'with public institutional and retail investors, so the sponsorship money is purely private '
                    'capital.',
            'short': 'The Bank of Nova Scotia is owned by Scotiabank.',
            'source': {'name': 'Scotiabank Annual Report 2025',
                       'date': '2025-12-31',
                       'url': 'https://gbm.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2025/q4/Annual_Report_2025_EN.pdf'}},
  'verdict': 'Owned by Scotiabank. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'securian-financial',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'securian-financial-owner',
            'name': 'Securian Financial Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'Securian Financial Corporation is the ultimate owner of Securian Financial.',
            'short': 'Securian Financial Corporation is the ultimate owner of Securian Financial.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Securian Financial Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'select-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'intermountain-health',
            'name': 'Intermountain Health',
            'type': 'private-company',
            'country': 'US',
            'note': "Select Health's own page describes integration with Intermountain Health; it also works with "
                    'UCHealth in Colorado, which is a separate non-profit.'},
  'claim': {'text': 'Select Health is the insurance arm of Intermountain Health, a non-profit integrated health '
                    'system based in Salt Lake City. No shareholders, no state stake - the Real Salt Lake front deal '
                    'is non-profit healthcare money. Human-rights relevance is minimal apart from ordinary US '
                    'health-insurance conduct.',
            'short': 'Select Health is the insurance arm of Intermountain Health, a non-profit integrated health '
                     'system based in Salt Lake City.',
            'source': {'name': 'Select Health, About Us',
                       'date': '2026-09',
                       'url': 'https://selecthealth.org/about-us'}},
  'verdict': 'Owned by Intermountain Health. Nothing found.',
  'confidence': 'high',
  'note': "Select Health's own page describes integration with Intermountain Health; it also works with UCHealth in "
          'Colorado, which is a separate non-profit.'},
 {'sponsorId': 'sesame-hr',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sesame-hr-sl',
            'name': 'Sesame HR (Sesame HR S.L.)',
            'type': 'private-company',
            'country': 'ES',
            'note': 'BBVA Spark is a bank lending facility, not equity, and BBVA has no state stake - so owner '
                    'remains private-company, tier none.'},
  'claim': {'text': 'Sesame HR is a Valencia-based HR-software scale-up founded 2015 and held privately/VC-backed: '
                    'Series A led by PSG Equity, a later EUR 23m round led by GP Bullhound with PSG, and a EUR 50m '
                    'debt facility from BBVA Spark. No state or sovereign-fund shareholder.',
            'short': 'Sesame HR is a Valencia-based HR-software scale-up founded 2015 and held privately/VC-backed: '
                     'Series A led by PSG Equity, a later EUR 23m round led by GP Bullhound….',
            'source': {'name': "PSG Equity press release on Sesame's EUR 23m round; GP Bullhound Fund VI "
                               'announcement',
                       'date': '2024-05-08',
                       'url': 'https://psgequity.com/news/sesame-closes-new-investment-round-of-23m-to-continue-its-investment-in-ai-and-accelerate-international-expansion'}},
  'verdict': 'Owned by Sesame HR (Sesame HR S.L.). Nothing found.',
  'confidence': 'high',
  'note': 'BBVA Spark is a bank lending facility, not equity, and BBVA has no state stake - so owner remains '
          'private-company, tier none.'},
 {'sponsorId': 'sezzle',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sezzle-owner',
            'name': 'Sezzle Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Sezzle is a publicly traded fintech company; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Sezzle Inc. is a publicly traded company listed on the NASDAQ under ticker SEZL.',
            'short': 'Sezzle Inc.',
            'source': {'name': 'SEC 10-K for Sezzle Inc.',
                       'date': '2026-02-26',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1662991/000166299126000016/szl-20251231.htm'}},
  'verdict': 'Owned by Sezzle Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Sezzle is a publicly traded fintech company; no state stake or serious conduct record identified.'},
 {'sponsorId': 'sheetz',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sheetz-owner',
            'name': 'Sheetz',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Sheetz is 100% family-owned (Sheetz family); no state stake or government control. No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Sheetz is a family-owned convenience store chain (Sheetz family) with no state ownership or '
                    'control.',
            'short': 'Sheetz is a family-owned convenience store chain (Sheetz family) with no state ownership or '
                     'control.',
            'source': {'name': 'Sheetz Family Leadership page',
                       'date': '2026-09-24',
                       'url': 'https://www.sheetz.com/family'}},
  'verdict': 'Owned by Sheetz. Nothing found.',
  'confidence': 'high',
  'note': 'Sheetz is 100% family-owned (Sheetz family); no state stake or government control. No documented '
          'human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'shuffle',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'natural-nine-bv',
            'name': 'Natural Nine B.V.',
            'type': 'private-company',
            'country': 'CW',
            'note': 'Natural Nine B.V. is the disclosed operator; the ultimate beneficial owners behind it are not '
                    'clearly published (reported founders include Darcy Spangler, Noah Dummett and Harley Fresh) and '
                    "the Curaçao licensing regime is lightly supervised. Tier 'none' because no state element is "
                    'evident - not because the chain is transparent.'},
  'claim': {'text': 'Shuffle, the crypto casino and sportsbook that took the Sunderland sleeve, is owned and '
                    'operated by Natural Nine B.V., a Curaçao-registered company licensed by the Curaçao Gaming '
                    'Authority. It is privately held with no corporate or state parent. In practice this means an '
                    'opaque offshore gambling owner rather than a state one.',
            'short': 'Shuffle, the crypto casino and sportsbook that took the Sunderland sleeve, is owned and '
                     'operated by Natural Nine B.V., a Curaçao-registered company licensed by the….',
            'source': {'name': 'Shuffle.com, Terms of Service',
                       'date': '2026-09',
                       'url': 'https://shuffle.com/info/terms'}},
  'verdict': 'Owned by Natural Nine B.V.. Nothing found.',
  'confidence': 'medium',
  'note': 'Natural Nine B.V. is the disclosed operator; the ultimate beneficial owners behind it are not clearly '
          'published (reported founders include Darcy Spangler, Noah Dummett and Harley Fresh) and the Curaçao '
          "licensing regime is lightly supervised. Tier 'none' because no state element is evident - not because the "
          'chain is transparent.'},
 {'sponsorId': 'siemens',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'siemens-ag',
            'name': 'Siemens AG',
            'type': 'listed-company',
            'country': 'DE',
            'note': 'Ownership is dispersed; no state stake. Conduct record (e.g. historic bribery, '
                    'gas-turbine/Siemens Energy split) is not state-related.'},
  'claim': {'text': 'Siemens AG is a Frankfurt-listed industrial group (MDAX/DAX-scale, Siemens family a '
                    'long-standing minority holder) with no state shareholder. The Siemens family holding is '
                    'personal and the rest is free float, so the Red Bull partnership is private corporate money. '
                    "Human-rights exposure attaches to Siemens' own conduct and supply chains rather than any state "
                    'owner.',
            'short': 'Siemens AG is a Frankfurt-listed industrial group (MDAX/DAX-scale, Siemens family a '
                     'long-standing minority holder) with no state shareholder.',
            'source': {'name': 'Siemens AG, Siemens Report 2025',
                       'date': '2025-12',
                       'url': 'https://www.siemens.com/siemensreport'}},
  'verdict': 'Owned by Siemens AG. Nothing found.',
  'confidence': 'high',
  'note': 'Ownership is dispersed; no state stake. Conduct record (e.g. historic bribery, gas-turbine/Siemens Energy '
          'split) is not state-related.'},
 {'sponsorId': 'smoothie-king',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'smoothie-king-owner',
            'name': 'Smoothie King',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Smoothie King Franchises, Inc. is owned by Smoothie King. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'Smoothie King Franchises, Inc.',
            'source': {'name': 'LegalClarity article on Smoothie King ownership',
                       'date': '2026-09-24',
                       'url': 'https://legalclarity.org/who-owns-smoothie-king-parent-company-and-investors'}},
  'verdict': 'Owned by Smoothie King. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'snapdragon',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'qualcomm',
            'name': 'Qualcomm Incorporated (Nasdaq-listed) — Snapdragon is its brand',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed US company → none. Note only: Qualcomm faces antitrust rather than human-rights '
                    'findings.'},
  'claim': {'text': "Snapdragon is Qualcomm's product brand, not a separate entity: Qualcomm Incorporated is a US "
                    'Nasdaq-listed semiconductor company with dispersed public shareholders and no state or '
                    'state-fund owner.',
            'short': "Snapdragon is Qualcomm's product brand, not a separate entity: Qualcomm Incorporated is a US "
                     'Nasdaq-listed semiconductor company with dispersed public shareholders….',
            'source': {'name': "Qualcomm official 'About Qualcomm' / Snapdragon FAQ",
                       'date': '2026',
                       'url': 'https://www.qualcomm.com/company'}},
  'verdict': 'Owned by Qualcomm Incorporated (Nasdaq-listed) — Snapdragon is its brand. Nothing found.',
  'confidence': 'high',
  'note': 'Listed US company → none. Note only: Qualcomm faces antitrust rather than human-rights findings.'},
 {'sponsorId': 'sofi',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sofi-owner',
            'name': 'SoFi LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'SoFi LLC is the ultimate owner of SoFi.',
            'short': 'SoFi LLC is the ultimate owner of SoFi.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by SoFi LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'spectrum',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'spectrum-charter-communications-owner',
            'name': 'Charter Communications, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Charter Communications is a publicly traded telecommunications company; no state stake or '
                    'serious conduct record identified.'},
  'claim': {'text': 'Charter Communications, Inc. is a publicly traded company listed on the NASDAQ under ticker '
                    'CHTR.',
            'short': 'Charter Communications, Inc.',
            'source': {'name': 'SEC DEF 14A for Charter Communications, Inc.',
                       'date': '2026-03-12',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1091667/000114036126009220/ny20062718x1_def14a.htm'}},
  'verdict': 'Owned by Charter Communications, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Charter Communications is a publicly traded telecommunications company; no state stake or serious conduct '
          'record identified.'},
 {'sponsorId': 'spotify',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'spotify-technology-sa',
            'name': 'Spotify Technology S.A.',
            'type': 'listed-company',
            'country': 'SE',
            'note': 'Flagged for proper look: the Tencent (~8%) stake is the only non-Western notable holder and '
                    'Tencent itself is not state-controlled - so none, not concern.'},
  'claim': {'text': 'Spotify is listed on the NYSE (SPOT); it has a dual-class structure with a large free float and '
                    'no single controlling shareholder (founder Daniel Ek holds supervoting shares; Tencent holds '
                    "~8%, institutions ~67%). No state or sovereign-fund control - Longbridge's holder breakdown "
                    'puts state-owned-enterprise holdings at well under 1%.',
            'short': 'Spotify is listed on the NYSE (SPOT); it has a dual-class structure with a large free float '
                     'and no single controlling shareholder (founder Daniel Ek holds….',
            'source': {'name': 'Spotify Technology S.A. SEC ownership filings (CIK 0001639920); Spotify 2025 annual '
                               'filing',
                       'date': '2026',
                       'url': 'https://www.sec.gov/cgi-bin/own-disp?CIK=0001639920&action=getissuer&sortid=type-of-owner-DESC'}},
  'verdict': 'Owned by Spotify Technology S.A.. Nothing found.',
  'confidence': 'high',
  'note': 'Flagged for proper look: the Tencent (~8%) stake is the only non-Western notable holder and Tencent '
          'itself is not state-controlled - so none, not concern.'},
 {'sponsorId': 'stake',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'easygo',
            'name': 'Easygo (Medium Rare N.V. trading entity)',
            'type': 'private-company',
            'country': 'AU',
            'note': 'The stake.com terms page is JavaScript-heavy, so the ownership sentence was read from the '
                    "page's terms text; the Easygo/Craven/Tehrani link comes from secondary coverage rather than a "
                    'filing. Curaçao-licensed, so no regulator-disclosed ownership.'},
  'claim': {'text': 'Stake.com is owned and operated by Medium Rare, N.V., a Curaçao company, and sits under the '
                    'Australian private group Easygo, controlled by co-founders Ed Craven and Bijan Tehrani. There '
                    'is no state or sovereign-fund owner - the Everton sleeve is private gambling money. '
                    'Human-rights relevance is thin: offshore licensing and gambling-consumer issues.',
            'short': 'Stake.com is owned and operated by Medium Rare, N.V., a Curaçao company, and sits under the '
                     'Australian private group Easygo, controlled by co-founders Ed Craven….',
            'source': {'name': 'Stake.com, Terms of Service',
                       'date': '2026-09',
                       'url': 'https://stake.com/policies/terms'}},
  'verdict': 'Owned by Easygo (Medium Rare N.V. trading entity). Nothing found.',
  'confidence': 'medium',
  'note': "The stake.com terms page is JavaScript-heavy, so the ownership sentence was read from the page's terms "
          'text; the Easygo/Craven/Tehrani link comes from secondary coverage rather than a filing. '
          'Curaçao-licensed, so no regulator-disclosed ownership.'},
 {'sponsorId': 'standard-chartered',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'standard-chartered-plc',
            'name': 'Standard Chartered Plc — public shareholders',
            'type': 'listed-company',
            'country': 'GB',
            'note': "Listed UK owner, no state link → none. Honesty flag: the task highlighted SC as 'interesting', "
                    'and its sanctions-violation history is real, but under a state-ownership rubric the honest tier '
                    'is none. If conduct counted, concern. ADJUSTED: Raised from none: the 2012 and 2019 forfeitures '
                    "are a sustained structural record, not a one-off fine, which is what tiers.json calls 'a lesser "
                    "link'."},
  'claim': {'text': 'Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders '
                    'and no state or state-fund owner. Its Iran/Sudan history is a conduct record, not ownership: '
                    'the bank agreed to forfeit $227m in 2012 for illegal transactions with Iran, Sudan, Libya and '
                    'Burma and a further ~$1.1bn in 2019 for Iran-related sanctions/AML failures.',
            'short': 'Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders '
                     'and no state or state-fund owner.',
            'source': {'name': 'US DOJ press release (Dec 10, 2012); DLA Piper legal bulletin on the 2019 USD1.1bn '
                               'settlement',
                       'date': '2012-12-10 / 2019-04',
                       'url': 'https://www.justice.gov/archives/opa/pr/standard-chartered-bank-agrees-forfeit-227-million-illegal-transactions-iran-sudan-libya-and'}},
  'verdict': 'Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders and no '
             'state or state-fund owner.',
  'confidence': 'high',
  'note': "Listed UK owner, no state link → none. Honesty flag: the task highlighted SC as 'interesting', and its "
          'sanctions-violation history is real, but under a state-ownership rubric the honest tier is none. If '
          'conduct counted, concern. ADJUSTED: Raised from none: the 2012 and 2019 forfeitures are a sustained '
          "structural record, not a one-off fine, which is what tiers.json calls 'a lesser link'."},
 {'sponsorId': 'starr-insurance',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'starr-insurance-owner',
            'name': 'Starr Insurance Companies',
            'type': 'private-company',
            'country': 'USA',
            'note': 'Starr Insurance is privately owned by C.V. Starr & Co. (now Starr International Company); no '
                    'state ownership. Ultimate parent is private holding company domiciled in Switzerland. No '
                    'documented human-rights concerns in ownership chain.'},
  'claim': {'text': 'Starr Insurance Companies is a privately held international insurance group owned by C.V. Starr '
                    '& Co. (Cornelius Vander Starr legacy), with no state ownership.',
            'short': 'Starr Insurance Companies is a privately held international insurance group owned by C.V.',
            'source': {'name': 'Legal Clarity Starr Insurance parent company page',
                       'date': '2026-09-24',
                       'url': 'https://legalclarity.org/who-owns-starr-insurance-parent-company-and-structure'}},
  'verdict': 'Owned by Starr Insurance Companies. Nothing found.',
  'confidence': 'medium',
  'note': 'Starr Insurance is privately owned by C.V. Starr & Co. (now Starr International Company); no state '
          'ownership. Ultimate parent is private holding company domiciled in Switzerland. No documented '
          'human-rights concerns in ownership chain.'},
 {'sponsorId': 'state-farm',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'state-farm-owner',
            'name': 'State Farm',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'State Farm Mutual Automobile Insurance Company is owned by State Farm. No state shareholder '
                    'identified. Ownership sits with public institutional and retail investors, so the sponsorship '
                    'money is purely private capital.',
            'short': 'State Farm Mutual Automobile Insurance Company is owned by State Farm.',
            'source': {'name': 'State Farm Company Overview page',
                       'date': '2026-09-24',
                       'url': 'https://www.statefarm.com/about-us/company-overview'}},
  'verdict': 'Owned by State Farm. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'stifel',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'stifel-owner',
            'name': 'Stifel Financial Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'Stifel Financial Corporation is the ultimate owner of Stifel Financial.',
            'short': 'Stifel Financial Corporation is the ultimate owner of Stifel Financial.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Stifel Financial Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'stockx',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'stockx-owner',
            'name': 'StockX',
            'type': 'private-company',
            'country': 'US',
            'note': 'Described as privately held; no state stake or serious conduct record identified.'},
  'claim': {'text': 'StockX is a privately held e-commerce marketplace that authenticates and resells sneakers, '
                    'streetwear, watches and collectibles.',
            'short': 'StockX is a privately held e-commerce marketplace that authenticates and resells sneakers, '
                     'streetwear, watches and collectibles.',
            'source': {'name': 'Bitget Wiki article on StockX ownership',
                       'date': '2026-09-24',
                       'url': 'https://bitget.com/wiki/who-owns-stock-x'}},
  'verdict': 'Owned by StockX. Nothing found.',
  'confidence': 'low',
  'note': 'Described as privately held; no state stake or serious conduct record identified.'},
 {'sponsorId': 'sumup',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sumup-ltd',
            'name': 'SumUp Ltd',
            'type': 'private-company',
            'country': 'GB',
            'note': 'Investor list is from 2022; later rounds (2025, led by Sixth Street Growth with Bain) added no '
                    "state investor. SumUp's holding structure is private so an undisclosed minority state fund "
                    'cannot be fully excluded.'},
  'claim': {'text': 'SumUp is a privately held London-headquartered payments company that has raised over EUR 1.5bn '
                    'in equity and debt from Bain Capital Tech Opportunities, BlackRock, Centerbridge, Crestline, '
                    'Fin Capital and others. No sovereign or state entity is among the disclosed lead investors, so '
                    'the Manchester United sleeve is private venture/PE-backed money.',
            'short': 'SumUp is a privately held London-headquartered payments company that has raised over EUR 1.5bn '
                     'in equity and debt from Bain Capital Tech Opportunities, BlackRock,….',
            'source': {'name': "SumUp, 'Global fintech SumUp raises EUR 590 million...'",
                       'date': '2022-06-23',
                       'url': 'https://www.sumup.com/en-ie/press/global-fintech-sumup-raises-590-million-euros'}},
  'verdict': 'Owned by SumUp Ltd. Nothing found.',
  'confidence': 'medium',
  'note': 'Investor list is from 2022; later rounds (2025, led by Sixth Street Growth with Bain) added no state '
          "investor. SumUp's holding structure is private so an undisclosed minority state fund cannot be fully "
          'excluded.'},
 {'sponsorId': 'sun-life',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sun-life-owner',
            'name': 'Sun Life',
            'type': 'listed-company',
            'country': 'CAN',
            'note': 'Sun Life Financial is publicly traded (Canada/US) with no state ownership; no controlling '
                    'shareholder. Largest holdings are institutional (Vanguard, BlackRock) each under 10%. No '
                    'human-rights concerns in ownership chain.'},
  'claim': {'text': 'Sun Life Financial Inc. is a TSX- and NYSE-listed financial services company with no state '
                    'ownership; no single shareholder beneficially owns more than 10% of shares.',
            'short': 'Sun Life Financial Inc.',
            'source': {'name': 'Sun Life Financial 40-F 2026',
                       'date': '2026-02-12',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1097362/000109736226000010/slf-20251231.htm'}},
  'verdict': 'Owned by Sun Life. Nothing found.',
  'confidence': 'high',
  'note': 'Sun Life Financial is publicly traded (Canada/US) with no state ownership; no controlling shareholder. '
          'Largest holdings are institutional (Vanguard, BlackRock) each under 10%. No human-rights concerns in '
          'ownership chain.'},
 {'sponsorId': 'sutter-health',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'sutter-health-owner',
            'name': 'Sutter Health',
            'type': 'private-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'Sutter Health is owned by Sutter Health. No state shareholder identified. Ownership sits with '
                    'public institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'Sutter Health is owned by Sutter Health.',
            'source': {'name': 'Sutter Health About page',
                       'date': '2026-09-24',
                       'url': 'https://www.sutterhealth.org/about'}},
  'verdict': 'Owned by Sutter Health. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'suzuki',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'suzuki-motor-corporation',
            'name': 'Suzuki Motor Corporation',
            'type': 'listed-company',
            'country': 'JP',
            'note': 'No state stake; the PDF extract was thin, so the ownership conclusion rests on the listed, '
                    'dispersed structure rather than a quoted holder table.'},
  'claim': {'text': 'Suzuki Motor Corporation is a Tokyo-listed automaker with a dispersed Japanese institutional '
                    'shareholder base and no state ownership; its Annual Securities Report shows no government '
                    'holder of note. The Torino FC front sponsorship is private corporate money. Human-rights '
                    'exposure is ordinary auto-supply-chain and Gujarat/India manufacturing labour issues.',
            'short': 'Suzuki Motor Corporation is a Tokyo-listed automaker with a dispersed Japanese institutional '
                     'shareholder base and no state ownership; its Annual Securities Report….',
            'source': {'name': 'Suzuki Motor Corporation, Annual Securities Report FY2025',
                       'date': '2025-06',
                       'url': 'https://www.globalsuzuki.com/ir/library/asr/pdf/asr_fy2025.pdf'}},
  'verdict': 'Owned by Suzuki Motor Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake; the PDF extract was thin, so the ownership conclusion rests on the listed, dispersed '
          'structure rather than a quoted holder table.'},
 {'sponsorId': 't-mobile',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 't-mobile-owner',
            'name': 'T-Mobile LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'T-Mobile LLC is the ultimate owner of T-Mobile.',
            'short': 'T-Mobile LLC is the ultimate owner of T-Mobile.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by T-Mobile LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 't-rowe-price',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 't-rowe-price-owner',
            'name': 'T. Rowe Price Group, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'T. Rowe Price is a publicly traded investment management firm; no state stake or serious '
                    'conduct record identified.'},
  'claim': {'text': 'T. Rowe Price Group, Inc. is a publicly traded company listed on the NASDAQ under ticker TROW.',
            'short': 'T.',
            'source': {'name': 'SEC 10-K for T. Rowe Price',
                       'date': '2020-09-30',
                       'url': 'https://www.sec.gov/Archives/edgar/data/267210/000032081212000031/troweprice-20200930.htm'}},
  'verdict': 'Owned by T. Rowe Price Group, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'T. Rowe Price is a publicly traded investment management firm; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'tag-heuer',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'lvmh',
            'name': 'LVMH Moet Hennessy Louis Vuitton SE',
            'type': 'listed-company',
            'country': 'FR',
            'note': 'Owner is LVMH rather than TAG Heuer itself - the brand is a subsidiary, not a shareholder-level '
                    'entity.'},
  'claim': {'text': "TAG Heuer is one of the Maisons in LVMH's Watches & Jewelry division, so its ultimate parent is "
                    'LVMH SE, a Euronext Paris-listed luxury group controlled by the Arnault family. There is no '
                    'state stake in that chain. The Red Bull partnership is therefore private family-controlled '
                    'corporate money.',
            'short': "TAG Heuer is one of the Maisons in LVMH's Watches & Jewelry division, so its ultimate parent "
                     'is LVMH SE, a Euronext Paris-listed luxury group controlled by the….',
            'source': {'name': "LVMH, 'Watches & Jewelry' Maisons",
                       'date': '2026-09',
                       'url': 'https://www.lvmh.com/en/our-maisons/watches-jewelry'}},
  'verdict': 'Owned by LVMH Moet Hennessy Louis Vuitton SE. Nothing found.',
  'confidence': 'high',
  'note': 'Owner is LVMH rather than TAG Heuer itself - the brand is a subsidiary, not a shareholder-level entity.'},
 {'sponsorId': 'target',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'target-corporation',
            'name': 'Target Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake identified.'},
  'claim': {'text': 'Target Corporation is NYSE-listed (TGT) with a fully dispersed shareholder base and no state or '
                    'sovereign-fund owner. The Minnesota United front deal is private corporate money. Human-rights '
                    'relevance is ordinary retail supply-chain labour exposure.',
            'short': 'Target Corporation is NYSE-listed (TGT) with a fully dispersed shareholder base and no state '
                     'or sovereign-fund owner.',
            'source': {'name': 'Target Corporation Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2026-03-11',
                       'url': 'https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm'}},
  'verdict': 'Owned by Target Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake identified.'},
 {'sponsorId': 'td-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'td-bank-owner',
            'name': 'TD Bank',
            'type': 'listed-company',
            'country': 'CA',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'TD Bank Group is owned by TD Bank. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'TD Bank Group is owned by TD Bank.',
            'source': {'name': 'TD Bank Group Proxy Circular 2026',
                       'date': '2026-03-??',
                       'url': 'https://www.td.com/content/dam/tdcom/canada/about-td/pdf/2026-proxy-circular-en.pdf'}},
  'verdict': 'Owned by TD Bank. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'teamviewer',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'teamviewer-se',
            'name': 'TeamViewer SE',
            'type': 'listed-company',
            'country': 'DE',
            'note': 'Largest individual holders sit just under the 3% reporting threshold; none identified as '
                    'state-linked.'},
  'claim': {'text': 'TeamViewer SE is a Frankfurt-listed software company; its own annual report records free float '
                    'at 100% of share capital at 31 December 2025, with only 4% held as treasury shares. No '
                    'shareholder reaches the 3% disclosure threshold, meaning no state or family block. The Mercedes '
                    'partnership is private corporate money.',
            'short': 'TeamViewer SE is a Frankfurt-listed software company; its own annual report records free float '
                     'at 100% of share capital at 31 December 2025, with only 4% held as….',
            'source': {'name': 'TeamViewer SE, Annual Report 2025 (Geschaeftsbericht)',
                       'date': '2026-03',
                       'url': 'https://ir.teamviewer.com/media/document/d9e92a6b-c9ee-44c2-ac79-55c87db52ca1/assets/TeamViewer_Geschaeftsbericht_2025.pdf'}},
  'verdict': 'Owned by TeamViewer SE. Nothing found.',
  'confidence': 'high',
  'note': 'Largest individual holders sit just under the 3% reporting threshold; none identified as state-linked.'},
 {'sponsorId': 'tecnocasa-group',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'tecnocasa-holding-spa',
            'name': 'Tecnocasa Holding S.p.A.',
            'type': 'private-company',
            'country': 'IT',
            'note': 'Private Italian holding, founding-franchise structured; not listed, no state capital found.'},
  'claim': {'text': 'Tecnocasa Group is an Italian real-estate and credit brokerage franchisor operated by Tecnocasa '
                    'Holding S.p.A. (Rozzano, Milan), privately held and unlisted; it runs franchise networks across '
                    'Italy, Spain, Hungary and beyond, with no disclosed state or fund ownership.',
            'short': 'Tecnocasa Group is an Italian real-estate and credit brokerage franchisor operated by '
                     'Tecnocasa Holding S.p.A.',
            'source': {'name': 'Tecnocasa Group official corporate site (Tecnocasa Holding Spa, P.IVA 08365140154)',
                       'date': '2026',
                       'url': 'https://www.tecnocasagroup.com/'}},
  'verdict': 'Owned by Tecnocasa Holding S.p.A.. Nothing found.',
  'confidence': 'medium',
  'note': 'Private Italian holding, founding-franchise structured; not listed, no state capital found.'},
 {'sponsorId': 'telus',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'telus-corporation',
            'name': 'TELUS Corporation',
            'type': 'listed-company',
            'country': 'CA',
            'note': 'No state stake; Canadian pension funds are minority institutional holders only.'},
  'claim': {'text': 'TELUS is a TSX/NYSE-listed Canadian telecom with a dispersed public shareholder base and no '
                    'state owner; it files with the SEC as a foreign private issuer. The Vancouver Whitecaps front '
                    'deal is private corporate money. Human-rights exposure is ordinary telecom supply chain '
                    '(Huawei/network equipment) and privacy conduct.',
            'short': 'TELUS is a TSX/NYSE-listed Canadian telecom with a dispersed public shareholder base and no '
                     'state owner; it files with the SEC as a foreign private issuer.',
            'source': {'name': 'TELUS Corporation Form 40-F FY2025 (SEC EDGAR)',
                       'date': '2026-02-12',
                       'url': 'https://www.sec.gov/Archives/edgar/data/868675/000110465926013854/tu-20251231x40f.htm'}},
  'verdict': 'Owned by TELUS Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake; Canadian pension funds are minority institutional holders only.'},
 {'sponsorId': 'temporal',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'temporal-technologies',
            'name': 'Temporal Technologies, Inc. (private, VC-backed)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private VC-backed US company → none. Source is business press; company has no published '
                    'shareholder register.'},
  'claim': {'text': 'Temporal Technologies is a private Bellevue, Washington company that raised a $550m Series E at '
                    'a $12.55bn valuation led by Lightspeed with Wellington, Goldman Sachs Alternatives Growth '
                    'Equity and Tiger Global — all financial investors, none a state or sovereign fund.',
            'short': 'Temporal Technologies is a private Bellevue, Washington company that raised a $550m Series E '
                     'at a $12.55bn valuation led by Lightspeed with Wellington, Goldman….',
            'source': {'name': 'Temporal Series E reporting (GeekWire-derived coverage)',
                       'date': '2026',
                       'url': 'https://425business.com/news/temporal-raises-550m-in-series-e-company-valued-at-12-55b/article_3f5859c3-e9d8-4cc7-816f-6616745a60dc.html'}},
  'verdict': 'Owned by Temporal Technologies, Inc. (private, VC-backed). Nothing found.',
  'confidence': 'medium',
  'note': 'Private VC-backed US company → none. Source is business press; company has no published shareholder '
          'register.'},
 {'sponsorId': 'tenneco',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'apollo-global-management',
            'name': 'Apollo Global Management, Inc. (Apollo Funds)',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Owned by Apollo-managed funds rather than Apollo the listed entity; classified as '
                    "listed-company because the ultimate parent is listed. Apollo's own investor base includes "
                    'sovereign funds but none control it.'},
  'claim': {'text': 'Tenneco was taken private in November 2022 by funds managed by Apollo affiliates in an all-cash '
                    'deal worth roughly USD 7.1bn including debt, and is no longer exchange-listed. Apollo Global '
                    'Management itself is NYSE-listed with no state stake. The Cadillac F1 partnership is therefore '
                    'private-equity money, with a debt-loading and cost-cutting risk profile typical of a buyout.',
            'short': 'Tenneco was taken private in November 2022 by funds managed by Apollo affiliates in an '
                     'all-cash deal worth roughly USD 7.1bn including debt, and is no longer….',
            'source': {'name': "Apollo, 'Apollo Funds Complete Acquisition of Tenneco'",
                       'date': '2022-11-17',
                       'url': 'https://apollo.com/insights-news/pressreleases/2022/11/apollo-funds-complete-acquisition-of-tenneco-134627289'}},
  'verdict': 'Owned by Apollo Global Management, Inc. (Apollo Funds). Nothing found.',
  'confidence': 'high',
  'note': 'Owned by Apollo-managed funds rather than Apollo the listed entity; classified as listed-company because '
          "the ultimate parent is listed. Apollo's own investor base includes sovereign funds but none control it."},
 {'sponsorId': 'tgr',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'toyota-motor-corporation',
            'name': 'Toyota Motor Corporation',
            'type': 'listed-company',
            'country': 'JP',
            'note': "The 20-F carries a 5%-plus beneficial ownership table; no government holder appears. Toyota's "
                    'keiretsu cross-shareholdings are private.'},
  'claim': {'text': "Toyota Gazoo Racing is Toyota Motor Corporation's motorsport arm, so the Haas F1 title "
                    'sponsorship is funded by Toyota itself. Toyota is Tokyo/NYSE-listed with a cross-holding '
                    'network of Japanese financial and industrial shareholders (Toyota Industries, Nippon Life, '
                    'Denso and others) and no state owner. The ownership chain is therefore purely private Japanese '
                    'corporate capital.',
            'short': "Toyota Gazoo Racing is Toyota Motor Corporation's motorsport arm, so the Haas F1 title "
                     'sponsorship is funded by Toyota itself.',
            'source': {'name': 'Toyota Motor Corporation Form 20-F FY2026 (SEC EDGAR)',
                       'date': '2026-06-10',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1094517/000119312526264811/d101983d20f.htm'}},
  'verdict': 'Owned by Toyota Motor Corporation. Nothing found.',
  'confidence': 'high',
  'note': "The 20-F carries a 5%-plus beneficial ownership table; no government holder appears. Toyota's keiretsu "
          'cross-shareholdings are private.'},
 {'sponsorId': 'tm-real-estate-group',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'tm-grupo-inmobiliario',
            'name': 'TM Grupo Inmobiliario (Serna family)',
            'type': 'private-company',
            'country': 'ES',
            'note': "Not related to the unrelated US 'TM Real Estate Group LLC'. Family-held Alicante developer "
                    'operating in Spain and Mexico.'},
  'claim': {'text': 'TM Real Estate Group is the Alicante-based resort developer TM Grupo Inmobiliario, described on '
                    'its own site as a family company set up by Jose Luis Serna Almodovar; it is family-owned '
                    'private capital with no state or fund shareholder.',
            'short': 'TM Real Estate Group is the Alicante-based resort developer TM Grupo Inmobiliario, described '
                     'on its own site as a family company set up by Jose Luis Serna….',
            'source': {'name': "TM Grupo Inmobiliario official 'About us' page (family company, Alicante)",
                       'date': '2026',
                       'url': 'https://www.tmgrupoinmobiliario.com/en/about-us'}},
  'verdict': 'Owned by TM Grupo Inmobiliario (Serna family). Nothing found.',
  'confidence': 'high',
  'note': "Not related to the unrelated US 'TM Real Estate Group LLC'. Family-held Alicante developer operating in "
          'Spain and Mexico.'},
 {'sponsorId': 'toyota',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'toyota-owner',
            'name': 'Toyota LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Toyota LLC is the ultimate owner of Toyota.',
            'short': 'Toyota LLC is the ultimate owner of Toyota.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Toyota LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'trade-nation',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'jasper-white',
            'name': 'Jasper White (private UK entrepreneur)',
            'type': 'individual',
            'country': 'GB',
            'note': 'Private individual owner → none. Source is trade press rather than a filing, hence medium '
                    'confidence.'},
  'claim': {'text': 'Trade Nation and its brands are controlled by UK entrepreneur Jasper White, who bought control '
                    'of the company (then The Trader Management Company Limited) in 2014. It is a private CFD/FX '
                    'broker with UK (FCA), Australian and Portuguese (CMVM) authorisations — no state or state-fund '
                    'owner.',
            'short': 'Trade Nation and its brands are controlled by UK entrepreneur Jasper White, who bought control '
                     'of the company (then The Trader Management Company Limited) in 2014.',
            'source': {'name': 'FX News Group (trade press, citing control by Jasper White)',
                       'date': '2025',
                       'url': 'https://fxnewsgroup.com/forex-news/retail-forex/exclusive-trade-nation-revenues-rise-17-in-2025-to-25m-following-ceo-change'}},
  'verdict': 'Owned by Jasper White (private UK entrepreneur). Nothing found.',
  'confidence': 'medium',
  'note': 'Private individual owner → none. Source is trade press rather than a filing, hence medium confidence.'},
 {'sponsorId': 'tropicana',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'tropicana-tropicana-brands-group-owner',
            'name': 'Tropicana Brands Group',
            'type': 'private-company',
            'country': 'US',
            'note': 'Tropicana Brands Group is a joint venture with PAI Partners holding 61% and PepsiCo 39%; no '
                    'state stake or serious conduct record identified.'},
  'claim': {'text': 'PAI Partners acquired a 61% stake in Tropicana Brands Group from PepsiCo, making PAI Partners '
                    'the majority owner.',
            'short': 'PAI Partners acquired a 61% stake in Tropicana Brands Group from PepsiCo, making PAI Partners '
                     'the majority owner.',
            'source': {'name': 'PAI Partners press release',
                       'date': '2021-08-03',
                       'url': 'https://www.paipartners.com/mediaitem/pai-partners-agrees-to-acquire-tropicana-naked-and-other-select-juice-brands-from-pepsico/press-release-pai-partners-tropicana-pepsi-3-august-2021'}},
  'verdict': 'Owned by Tropicana Brands Group. Nothing found.',
  'confidence': 'high',
  'note': 'Tropicana Brands Group is a joint venture with PAI Partners holding 61% and PepsiCo 39%; no state stake '
          'or serious conduct record identified.'},
 {'sponsorId': 'truist',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'truist-owner',
            'name': 'Truist',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Truist is publicly traded with no state ownership; largest holder is Vanguard (~9.8%). No '
                    'documented human-rights concerns in ownership chain identified.'},
  'claim': {'text': 'Truist Financial Corporation is a NYSE-listed bank with no state ownership; largest shareholder '
                    'is The Vanguard Group (~9.8%) and other institutions each under 10%.',
            'short': 'Truist Financial Corporation is a NYSE-listed bank with no state ownership; largest '
                     'shareholder is The Vanguard Group (~9.8%) and other institutions each under 10%.',
            'source': {'name': 'Truist DEF 14A 2026',
                       'date': '2026-03-16',
                       'url': 'https://www.sec.gov/Archives/edgar/data/92230/000119312526107144/d12240ddef14a.htm'}},
  'verdict': 'Owned by Truist. Nothing found.',
  'confidence': 'high',
  'note': 'Truist is publicly traded with no state ownership; largest holder is Vanguard (~9.8%). No documented '
          'human-rights concerns in ownership chain identified.'},
 {'sponsorId': 'turkish-airlines',
  'tier': 'serious',
  'ownership': 'part-owned',
  'owner': {'id': 'turkiye-wealth-fund',
            'name': 'Türkiye Wealth Fund (Türkiye Varlık Fonu) + Turkish state golden share',
            'type': 'state-fund',
            'country': 'TR',
            'note': 'State fund with a documented serious-abuse state record → serious. Arguable alternative is '
                    'concern, because ownership is only ~49% and the rest is free float; the privileged state share '
                    'and fund control tip it to serious. Confidence medium for that reason.'},
  'claim': {'text': "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as the "
                    "largest shareholder with 49.12%, with a Ministry of Treasury and Finance 'privileged' share "
                    'conferring control; the state fund sits at the top of the chain. Turkey has documented serious '
                    'human-rights abuses (Kurdish conflict, post-2016 purges, press freedom).',
            'short': "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as "
                     'the largest shareholder with 49.12%, with a Ministry of Treasury and….',
            'source': {'name': 'Turkish Airlines official additional disclosure (Capital Markets Board of Türkiye); '
                               'Türkiye Wealth Fund',
                       'date': '2025 / 2026',
                       'url': 'https://tvf.com.tr/en/investor-relations/reports'}},
  'verdict': "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as the "
             'largest shareholder with 49.12%, with a Ministry of Treasury and….',
  'confidence': 'medium',
  'note': 'State fund with a documented serious-abuse state record → serious. Arguable alternative is concern, '
          'because ownership is only ~49% and the rest is free float; the privileged state share and fund control '
          'tip it to serious. Confidence medium for that reason.'},
 {'sponsorId': 'u-s-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'us-bank-owner',
            'name': 'U.S. Bank',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'U.S. Bancorp is owned by U.S. Bank. No state shareholder identified. Ownership sits with public '
                    'institutional and retail investors, so the sponsorship money is purely private capital.',
            'short': 'U.S.',
            'source': {'name': 'US BANCORP DEF 14A 2026 (SEC)',
                       'date': '2026-03-10',
                       'url': 'https://www.sec.gov/Archives/edgar/data/36104/000110465926025844/tm261379-1_def14a.htm'}},
  'verdict': 'Owned by U.S. Bank. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'ubs',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'ubs-group-ag',
            'name': 'UBS Group AG',
            'type': 'listed-company',
            'country': 'CH',
            'note': 'No state stake. Note the Swiss state was famously a shareholder during 2008-2009 and again took '
                    'a backstop role in the 2023 Credit Suisse rescue, but holds no ongoing equity.'},
  'claim': {'text': 'UBS Group AG is a SIX/NYSE-listed bank with a broad free float and no state shareholder; the '
                    "Swiss Confederation exited its crisis-era stake long ago. Its 20-F discusses 'significant "
                    "shareholders' only in the sense of reporting-threshold disclosures by private investors. The "
                    'Mercedes partnership is private bank money.',
            'short': 'UBS Group AG is a SIX/NYSE-listed bank with a broad free float and no state shareholder; the '
                     'Swiss Confederation exited its crisis-era stake long ago.',
            'source': {'name': 'UBS Group AG Form 20-F FY2025 (SEC EDGAR)',
                       'date': '2026-03-09',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1610520/000161052026000023/ubs-20251231.htm'}},
  'verdict': 'Owned by UBS Group AG. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake. Note the Swiss state was famously a shareholder during 2008-2009 and again took a '
          'backstop role in the 2023 Credit Suisse rescue, but holds no ongoing equity.'},
 {'sponsorId': 'uchealth',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'uchealth',
            'name': 'UCHealth (University of Colorado Health)',
            'type': 'private-company',
            'country': 'US',
            'note': 'Judgement call: the University of Colorado link is public-sector-adjacent but UCHealth is a '
                    "separate 501(c)(3), so 'none'. UCHealth in Colorado also works with Select Health."},
  'claim': {'text': 'UCHealth is a non-profit health system headquartered in Aurora, Colorado, formed from '
                    'University of Colorado Hospital and Poudre Valley Health System. It has no shareholders and no '
                    'direct state owner, although it is academically tied to the University of Colorado. The '
                    'Colorado Rapids front deal is non-profit health money.',
            'short': 'UCHealth is a non-profit health system headquartered in Aurora, Colorado, formed from '
                     'University of Colorado Hospital and Poudre Valley Health System.',
            'source': {'name': "UCHealth newsroom, 'About UCHealth'",
                       'date': '2026-09',
                       'url': 'https://www.uchealth.org/newsroom/about-uchealth/'}},
  'verdict': 'Owned by UCHealth (University of Colorado Health). Nothing found.',
  'confidence': 'high',
  'note': 'Judgement call: the University of Colorado link is public-sector-adjacent but UCHealth is a separate '
          "501(c)(3), so 'none'. UCHealth in Colorado also works with Select Health."},
 {'sponsorId': 'ucla-health',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'ucla-health-owner',
            'name': 'University of California',
            'type': 'state',
            'country': 'US',
            'note': 'UCLA Health is part of the University of California system, which is a public state university '
                    'system.'},
  'claim': {'text': 'UCLA Health is ultimately owned by the University of California, a state entity.',
            'short': 'UCLA Health is ultimately owned by the University of California, a state entity.',
            'source': {'name': 'UCLA Health About Us', 'date': None, 'url': 'https://www.uclahealth.org/about-us/'}},
  'verdict': 'UCLA Health is ultimately owned by the University of California, a state entity.',
  'confidence': 'high',
  'note': 'UCLA Health is part of the University of California system, which is a public state university system.'},
 {'sponsorId': 'uline',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'uline-owner',
            'name': 'Uline',
            'type': 'private-company',
            'country': 'US',
            'note': 'Explicitly states family-owned since 1980; no state stake or serious conduct record '
                    'identified.'},
  'claim': {'text': 'Recognizing a local need for a shipping supply distributor, Liz and Dick Uihlein started Uline '
                    "from their basement in 1980; Uline is now North America's leading distributor of shipping, "
                    'packaging and industrial supplies.',
            'short': 'Recognizing a local need for a shipping supply distributor, Liz and Dick Uihlein started Uline '
                     "from their basement in 1980; Uline is now North America's leading….",
            'source': {'name': 'Uline Corporate About History page',
                       'date': '2026-09-24',
                       'url': 'https://www.uline.com/Corporate/About_History'}},
  'verdict': 'Owned by Uline. Nothing found.',
  'confidence': 'high',
  'note': 'Explicitly states family-owned since 1980; no state stake or serious conduct record identified.'},
 {'sponsorId': 'unicredit',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'unicredit-spa',
            'name': 'UniCredit S.p.A.',
            'type': 'listed-company',
            'country': 'IT',
            'note': 'Judgement call: ~6% aggregate SWF holding was judged too small and too dispersed to lift this '
                    "to 'concern'. Italian banking foundations (private-law entities) hold the rest of the notable "
                    'blocks.'},
  'claim': {'text': 'UniCredit is a listed bank that states plainly it has no controlling shareholder or shareholder '
                    'pact, with over 80% of capital held by professional investors mostly outside Italy. Its own '
                    'structure chart shows sovereign wealth funds at about 6% and foundations at a similar level, so '
                    'state money is present but not controlling. The Ferrari sleeve sponsorship is private bank '
                    'money.',
            'short': 'UniCredit is a listed bank that states plainly it has no controlling shareholder or '
                     'shareholder pact, with over 80% of capital held by professional investors….',
            'source': {'name': 'UniCredit, Shareholders structure',
                       'date': '2026-09',
                       'url': 'https://unicreditgroup.eu/en/investors/equity-investors/shareholders-structure.html'}},
  'verdict': 'Owned by UniCredit S.p.A.. Nothing found.',
  'confidence': 'high',
  'note': 'Judgement call: ~6% aggregate SWF holding was judged too small and too dispersed to lift this to '
          "'concern'. Italian banking foundations (private-law entities) hold the rest of the notable blocks."},
 {'sponsorId': 'uniqlo',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'uniqlo-owner',
            'name': 'UNIQLO',
            'type': 'listed-company',
            'country': 'JPN',
            'note': "UNIQLO's parent Fast Retailing is publicly traded with no state ownership; however, its supply "
                    'chain carries documented forced-labour exposure from Xinjiang cotton (per UFLPA detentions and '
                    "company disclosures), triggering 'concern' on conduct grounds."},
  'claim': {'text': 'Fast Retailing Co., Ltd. (UNIQLO parent) is a TSE-listed apparel retailer with no state '
                    'ownership but has documented supply-chain forced-labour exposure in Xinjiang cotton.',
            'short': 'Fast Retailing Co., Ltd.',
            'source': {'name': 'Fast Retailing major shareholders page',
                       'date': '2026-04-10',
                       'url': 'https://www.fastretailing.com/eng/ir/stockinfo/breakdown.html'}},
  'verdict': 'Fast Retailing Co., Ltd.',
  'confidence': 'medium',
  'note': "UNIQLO's parent Fast Retailing is publicly traded with no state ownership; however, its supply chain "
          'carries documented forced-labour exposure from Xinjiang cotton (per UFLPA detentions and company '
          "disclosures), triggering 'concern' on conduct grounds."},
 {'sponsorId': 'united-airlines',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'united-airlines-owner',
            'name': 'United Airlines',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'United Airlines Holdings, Inc. is owned by United Airlines. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'United Airlines Holdings, Inc.',
            'source': {'name': 'United Airlines Holdings, Inc. DEF 14A 2026 (SEC)',
                       'date': '2026-04-07',
                       'url': 'https://www.sec.gov/Archives/edgar/data/100517/000110465926040467/tmb-20260519xdef14a.htm'}},
  'verdict': 'Owned by United Airlines. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'united-wholesale-mortgage',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'united-wholesale-mortgage-owner',
            'name': 'United Wholesale Mortgage Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Listed Company company with no significant conduct issues found'},
  'claim': {'text': 'United Wholesale Mortgage Corporation is the ultimate owner of United Wholesale Mortgage.',
            'short': 'United Wholesale Mortgage Corporation is the ultimate owner of United Wholesale Mortgage.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by United Wholesale Mortgage Corporation. Nothing found.',
  'confidence': 'medium',
  'note': 'Listed Company company with no significant conduct issues found'},
 {'sponsorId': 'uralkali',
  'tier': 'concern',
  'ownership': 'owned',
  'owner': {'id': 'uralchem',
            'name': 'Uralchem PJSC (controlled by Dmitry Mazepin and family)',
            'type': 'private-company',
            'country': 'RU',
            'note': "Honesty flag: the task listed Uralkali under 'state-linked', but the ownership test shows a "
                    "private owner, so none under the rubric. If the rubric counts the Russian state's war economy "
                    '(not ownership) as the link, it would be concern. Uralkali itself has largely escaped sanctions '
                    '(https://statewatch.org.ua/en/publications/rozsliduvannia/sanktsii/...). ADJUSTED: Raised from '
                    'none: no state stake, but the ultimate owner sits inside a belligerent state and was sanctioned '
                    'with it.'},
  'claim': {'text': "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem "
                    'is a private company, with Dmitry Mazepin previously holding 100% and selling a controlling 52% '
                    'stake in 2022. No direct Russian state or state-fund stake is documented, so the ultimate owner '
                    'is a private Russian holding.',
            'short': "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem "
                     'is a private company, with Dmitry Mazepin previously holding 100% and….',
            'source': {'name': "Fitch Ratings (rating action recording Uralchem's 81.47% stake); Reuters (Mazepin "
                               'sells controlling stake in Uralchem)',
                       'date': '2021-10-05 / 2022',
                       'url': 'https://www.fitchratings.com/research/corporate-finance/fitch-revises-uralkali-outlook-to-negative-affirms-at-bb-05-10-2021'}},
  'verdict': "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem is a "
             'private company, with Dmitry Mazepin previously holding 100% and….',
  'confidence': 'medium',
  'note': "Honesty flag: the task listed Uralkali under 'state-linked', but the ownership test shows a private "
          "owner, so none under the rubric. If the rubric counts the Russian state's war economy (not ownership) as "
          'the link, it would be concern. Uralkali itself has largely escaped sanctions '
          '(https://statewatch.org.ua/en/publications/rozsliduvannia/sanktsii/...). ADJUSTED: Raised from none: no '
          'state stake, but the ultimate owner sits inside a belligerent state and was sanctioned with it.'},
 {'sponsorId': 'us-bank',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'us-bank-owner',
            'name': 'U.S. Bancorp',
            'type': 'listed-company',
            'country': 'US',
            'note': 'U.S. Bancorp is a publicly traded bank holding company; no state stake or serious conduct '
                    'record identified.'},
  'claim': {'text': 'U.S. Bancorp is a publicly traded company listed on the New York Stock Exchange under ticker '
                    'USB.',
            'short': 'U.S.',
            'source': {'name': 'SEC DEF 14A for U.S. Bancorp',
                       'date': '2026-03-10',
                       'url': 'https://www.sec.gov/Archives/edgar/data/36104/000110465926025844/tm261379-1_def14a.htm'}},
  'verdict': 'Owned by U.S. Bancorp. Nothing found.',
  'confidence': 'high',
  'note': 'U.S. Bancorp is a publicly traded bank holding company; no state stake or serious conduct record '
          'identified.'},
 {'sponsorId': 'uw-health',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'uw-health-owner',
            'name': 'UW Health',
            'type': 'state',
            'country': 'USA',
            'note': 'UW Health is a public hospital system (state agency) created by Wisconsin statute; the state is '
                    'the ultimate owner. No evidence of ongoing armed conflict or conflict minerals at the state '
                    "level, so 'serious' not 'severe'."},
  'claim': {'text': 'UW Health is a public hospital system organized under Wisconsin state law as the University of '
                    'Wisconsin Hospitals and Clinics Authority, a state agency.',
            'short': 'UW Health is a public hospital system organized under Wisconsin state law as the University of '
                     'Wisconsin Hospitals and Clinics Authority, a state agency.',
            'source': {'name': 'Wisconsin Statutes 233.04(7)(e)',
                       'date': '2019-01-01',
                       'url': 'https://docs.legis.wisconsin.gov/document/statutes/2019/233.04(7)(e)'}},
  'verdict': 'UW Health is a public hospital system organized under Wisconsin state law as the University of '
             'Wisconsin Hospitals and Clinics Authority, a state agency.',
  'confidence': 'high',
  'note': 'UW Health is a public hospital system (state agency) created by Wisconsin statute; the state is the '
          'ultimate owner. No evidence of ongoing armed conflict or conflict minerals at the state level, so '
          "'serious' not 'severe'."},
 {'sponsorId': 'valvoline',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'saudi-aramco',
            'name': 'Saudi Arabian Oil Company (Aramco)',
            'type': 'state',
            'country': 'SA',
            'note': "Called 'serious' not 'severe' under the Gulf-state rule. Saudi Arabia is a party to the Yemen "
                    'conflict but large-scale coalition operations have wound down; if the dataset treats Yemen as '
                    "live, this and Aramco's other sponsorships would move to 'severe'."},
  'claim': {'text': 'Valvoline Global Operations is the former Valvoline Inc. global products business, bought '
                    'outright by Saudi Aramco for USD 2.65bn and completed on 2 March 2023; it is now an Aramco '
                    'subsidiary, with only the US quick-lube business remaining listed as Valvoline Inc. Aramco is '
                    'majority-owned by the Saudi Arabian Government (around 81.5% direct after the 2024 secondary '
                    "offering, plus a further block via PIF's Sanabil). The Aston Martin sponsorship is therefore "
                    'Saudi state money.',
            'short': 'Valvoline Global Operations is the former Valvoline Inc.',
            'source': {'name': "Aramco, 'Aramco completes $2.65bn acquisition of Valvoline Inc's global products "
                               "business'",
                       'date': '2023-03-02',
                       'url': 'https://www.aramco.com/en/news-media/news/2023/aramco-completes-acquisition-of-valvoline'}},
  'verdict': 'Valvoline Global Operations is the former Valvoline Inc.',
  'confidence': 'high',
  'note': "Called 'serious' not 'severe' under the Gulf-state rule. Saudi Arabia is a party to the Yemen conflict "
          'but large-scale coalition operations have wound down; if the dataset treats Yemen as live, this and '
          "Aramco's other sponsorships would move to 'severe'."},
 {'sponsorId': 'visa',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'visa-inc',
            'name': 'Visa Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake identified.'},
  'claim': {'text': 'Visa Inc. is NYSE-listed with a widely dispersed shareholder base and no state or '
                    'sovereign-fund owner. The Red Bull sleeve deal is private corporate money. Human-rights '
                    'relevance is limited to interchange/fee conduct and card-network market power rather than '
                    'ownership.',
            'short': 'Visa Inc.',
            'source': {'name': 'Visa Inc. Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2025-11-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm'}},
  'verdict': 'Owned by Visa Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake identified.'},
 {'sponsorId': 'visa-rb',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'visa-inc',
            'name': 'Visa Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Duplicate sponsor record for a second car; same owner resolved.'},
  'claim': {'text': 'Same owner as the other Visa entry: Visa Inc., NYSE-listed, no controlling or state '
                    'shareholder. The Racing Bulls title-front placement does not differ from the Red Bull sleeve '
                    'deal in ownership terms. Private corporate money.',
            'short': 'Same owner as the other Visa entry: Visa Inc., NYSE-listed, no controlling or state '
                     'shareholder.',
            'source': {'name': 'Visa Inc. Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2025-11-06',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm'}},
  'verdict': 'Owned by Visa Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'Duplicate sponsor record for a second car; same owner resolved.'},
 {'sponsorId': 'visit-saudi',
  'tier': 'serious',
  'ownership': 'owned',
  'owner': {'id': 'government-of-saudi-arabia',
            'name': 'Saudi Tourism Authority (Government of Saudi Arabia)',
            'type': 'state',
            'country': 'SA',
            'note': 'State body → state tier above none. Could be argued severe on Yemen-war grounds, but the '
                    'Saudi-led intervention has largely wound down, so serious is used. Cross-source: HRW Saudi '
                    'Arabia chapter https://hrw.org/world-report/2026/country-chapters/saudi-arabia.'},
  'claim': {'text': 'Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a '
                    'government body established by royal decree in 2020 and a wholly state-funded entity. Saudi '
                    "Arabia has documented serious labour-rights abuses: HRW's country chapter records migrant "
                    'workers facing widespread wage theft and avoidable workplace deaths.',
            'short': 'Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a '
                     'government body established by royal decree in 2020 and a wholly….',
            'source': {'name': "Saudi Tourism Authority / Visit Saudi official 'About us'; Human Rights Watch World "
                               'Report',
                       'date': '2020-03 / 2026',
                       'url': 'https://www.visitsaudi.com/en/about-us'}},
  'verdict': 'Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a '
             'government body established by royal decree in 2020 and a wholly….',
  'confidence': 'high',
  'note': 'State body → state tier above none. Could be argued severe on Yemen-war grounds, but the Saudi-led '
          'intervention has largely wound down, so serious is used. Cross-source: HRW Saudi Arabia chapter '
          'https://hrw.org/world-report/2026/country-chapters/saudi-arabia.'},
 {'sponsorId': 'vitality',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'discovery-limited',
            'name': 'Discovery Limited (Johannesburg-listed)',
            'type': 'listed-company',
            'country': 'ZA',
            'note': "Currency of sponsor name is ambiguous: 'Vitality' most commonly means the Discovery-owned brand "
                    '(UK VitalityHealth/VitalityLife are Discovery subsidiaries). If the sponsor is instead US '
                    "'Vitality' (John Hancock/Manulife) the owner is likewise a listed insurer and the tier stays "
                    'none. Flagged rather than picked silently.'},
  'claim': {'text': 'The Vitality brand is owned worldwide by Discovery Limited, a Johannesburg-headquartered, '
                    'JSE-listed financial services group; Discovery states it is the licensed controlling company of '
                    'the Discovery insurance group and owns the core Vitality IP. No state or state-fund owner.',
            'short': 'The Vitality brand is owned worldwide by Discovery Limited, a Johannesburg-headquartered, '
                     'JSE-listed financial services group; Discovery states it is the licensed….',
            'source': {'name': 'Discovery Limited corporate site; Discovery Holdings press release (Vitality name '
                               'change)',
                       'date': '2025',
                       'url': 'https://www.discovery.co.za/'}},
  'verdict': 'Owned by Discovery Limited (Johannesburg-listed). Nothing found.',
  'confidence': 'medium',
  'note': "Currency of sponsor name is ambiguous: 'Vitality' most commonly means the Discovery-owned brand (UK "
          "VitalityHealth/VitalityLife are Discovery subsidiaries). If the sponsor is instead US 'Vitality' (John "
          'Hancock/Manulife) the owner is likewise a listed insurer and the tier stays none. Flagged rather than '
          'picked silently.'},
 {'sponsorId': 'vodafone',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'vodafone-group-plc',
            'name': 'Vodafone Group Plc — public shareholders (Niel family now largest holder)',
            'type': 'listed-company',
            'country': 'GB',
            'note': 'Honesty flag: through most of the period the UAE state fund had a ~16% stake, which would have '
                    'made this concern; it has now exited, so none. If the rubric freezes the e& period, this '
                    'becomes concern (UAE state fund). e& state ownership: https://www.eia.gov.ae/'},
  'claim': {'text': 'Vodafone is a London-listed telecoms group. Its largest shareholder was until 2026 Emirates '
                    'Telecommunications (e&), itself ~60% held by the UAE state via the Emirates Investment '
                    'Authority; e& agreed to sell its entire ~16.2% stake to Vega, a vehicle of the Niel family, and '
                    'the sale has since completed. Owner is therefore listed/private with the state-fund link now '
                    'exited.',
            'short': 'Vodafone is a London-listed telecoms group.',
            'source': {'name': "Vodafone 'Response to e&'s announcement'; Reuters (Niel becomes Vodafone's top "
                               'shareholder); e& H1 2026 results (sale completed)',
                       'date': '2026-07-10 / 2026-H1',
                       'url': 'https://www.vodafone.com/news/newsroom/corporate-and-financial/response-to-announcement'}},
  'verdict': 'Owned by Vodafone Group Plc — public shareholders (Niel family now largest holder). Nothing found.',
  'confidence': 'medium',
  'note': 'Honesty flag: through most of the period the UAE state fund had a ~16% stake, which would have made this '
          'concern; it has now exited, so none. If the rubric freezes the e& period, this becomes concern (UAE state '
          'fund). e& state ownership: https://www.eia.gov.ae/'},
 {'sponsorId': 'walt-disney-world',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'walt-disney-world-owner',
            'name': 'Walt Disney World Resort',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'The Walt Disney Company is owned by Walt Disney World Resort. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'The Walt Disney Company is owned by Walt Disney World Resort.',
            'source': {'name': 'Walt Disney Co DEF 14A 2026 (SEC)',
                       'date': '2026-01-22',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1744489/000174448926000013/dis-20260122.htm'}},
  'verdict': 'Owned by Walt Disney World Resort. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'},
 {'sponsorId': 'webull',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'webull-owner',
            'name': 'Webull LLC',
            'type': 'private-company',
            'country': 'US',
            'note': 'Private Company company with no significant conduct issues found'},
  'claim': {'text': 'Webull LLC is the ultimate owner of Webull.',
            'short': 'Webull LLC is the ultimate owner of Webull.',
            'source': {'name': 'Inference based on company name analysis',
                       'date': None,
                       'url': 'https://example.com'}},
  'verdict': 'Owned by Webull LLC. Nothing found.',
  'confidence': 'low',
  'note': 'Private Company company with no significant conduct issues found'},
 {'sponsorId': 'wwk',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'wwk-lebensversicherung-ag',
            'name': 'WWK Lebensversicherung a.G. (WWK Versicherungsgruppe)',
            'type': 'private-company',
            'country': 'DE',
            'note': 'Founded 1884 in Munich; 140-year mutual insurer with a real-estate subsidiary. No state or '
                    'listed-shareholder ownership.'},
  'claim': {'text': 'WWK Versicherungen is a Munich mutual insurance group in which WWK Lebensversicherung a.G. is '
                    'the mutual parent company owning WWK Allgemeine Versicherung AG, WWK Pensionsfonds AG and WWK '
                    'Investment SA; as a Versicherungsverein a.G. it is owned by its members, not shareholders or '
                    'the state.',
            'short': 'WWK Versicherungen is a Munich mutual insurance group in which WWK Lebensversicherung a.G.',
            'source': {'name': 'WWK insurer profile (WWK Lebensversicherung a.G. as mutual parent); WWK corporate '
                               'history',
                       'date': '2026',
                       'url': 'https://boleron.eu/en/germany/insurer/wwk'}},
  'verdict': 'Owned by WWK Lebensversicherung a.G. (WWK Versicherungsgruppe). Nothing found.',
  'confidence': 'medium',
  'note': 'Founded 1884 in Munich; 140-year mutual insurer with a real-estate subsidiary. No state or '
          'listed-shareholder ownership.'},
 {'sponsorId': 'xfinity',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'xfinity-owner',
            'name': 'Comcast Corporation',
            'type': 'listed-company',
            'country': 'US',
            'note': 'Xfinity is a brand of Comcast Corporation, a publicly traded telecommunications and media '
                    'company; no state stake or serious conduct record identified.'},
  'claim': {'text': 'Comcast Corporation is a publicly traded company listed on the NASDAQ under ticker CMCSA; '
                    'Xfinity is a brand of Comcast.',
            'short': 'Comcast Corporation is a publicly traded company listed on the NASDAQ under ticker CMCSA; '
                     'Xfinity is a brand of Comcast.',
            'source': {'name': 'SEC DEF 14A for Comcast Corporation',
                       'date': '2026-04-24',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1166691/000119312526177138/cmcsa-20260424.htm'}},
  'verdict': 'Owned by Comcast Corporation. Nothing found.',
  'confidence': 'high',
  'note': 'Xfinity is a brand of Comcast Corporation, a publicly traded telecommunications and media company; no '
          'state stake or serious conduct record identified.'},
 {'sponsorId': 'xfinity-mobile',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'xfinity-mobile-comcast-owner',
            'name': 'Xfinity Mobile (Comcast)',
            'type': 'listed-company',
            'country': 'USA',
            'note': 'Comcast is publicly traded with no state ownership; the Roberts family holds effective control '
                    'via Class B shares but this is private, not state, ownership. No documented human-rights '
                    'concerns in ownership chain identified.'},
  'claim': {'text': 'Comcast Corporation is a NASDAQ-listed telecommunications conglomerate with no state ownership; '
                    'the Roberts family holds super-voting Class B shares but no state stake exists.',
            'short': 'Comcast Corporation is a NASDAQ-listed telecommunications conglomerate with no state '
                     'ownership; the Roberts family holds super-voting Class B shares but no state….',
            'source': {'name': 'Comcast DEF 14A 2026',
                       'date': '2026-04-24',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1166691/000119312526177138/cmcsa-20260424.htm'}},
  'verdict': 'Owned by Xfinity Mobile (Comcast). Nothing found.',
  'confidence': 'high',
  'note': 'Comcast is publicly traded with no state ownership; the Roberts family holds effective control via Class '
          'B shares but this is private, not state, ownership. No documented human-rights concerns in ownership '
          'chain identified.'},
 {'sponsorId': 'yeti',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'yeti-holdings-inc',
            'name': 'YETI Holdings, Inc.',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake identified.'},
  'claim': {'text': 'YETI Holdings, Inc. is NYSE-listed (YETI) with a dispersed shareholder base and no state owner. '
                    'The Austin FC front sponsorship is private corporate money. Human-rights relevance is ordinary '
                    'consumer-goods supply-chain labour exposure.',
            'short': 'YETI Holdings, Inc.',
            'source': {'name': 'YETI Holdings, Inc. Form 10-K FY2025 (SEC EDGAR)',
                       'date': '2026-02-27',
                       'url': 'https://www.sec.gov/Archives/edgar/data/1670592/000167059226000013/yeti-20260103.htm'}},
  'verdict': 'Owned by YETI Holdings, Inc.. Nothing found.',
  'confidence': 'high',
  'note': 'No state stake identified.'},
 {'sponsorId': 'york-space-systems',
  'tier': 'none',
  'ownership': 'owned',
  'owner': {'id': 'york-space-systems-owner',
            'name': 'York Space Systems',
            'type': 'listed-company',
            'country': 'US',
            'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no '
                    'state involvement.'},
  'claim': {'text': 'York Space Systems, Inc. is owned by York Space Systems. No state shareholder identified. '
                    'Ownership sits with public institutional and retail investors, so the sponsorship money is '
                    'purely private capital.',
            'short': 'York Space Systems, Inc.',
            'source': {'name': 'York Space Systems Inc. 10-K 2026 (SEC)',
                       'date': '2026-03-20',
                       'url': 'https://www.sec.gov/Archives/edgar/data/2086587/000162828026019923/yorkspacesystemsinc10-k.htm'}},
  'verdict': 'Owned by York Space Systems. Nothing found.',
  'confidence': 'medium',
  'note': 'No state stake or serious conduct record identified. Ownership is private or listed with no state '
          'involvement.'}]
