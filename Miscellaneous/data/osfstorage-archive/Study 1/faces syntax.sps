

** Agreeableness - Female

IF  (AFF_LH_Q=1 | AFF_RH_Q=2) agreeableness_f=1.
EXECUTE.

IF  (AFF_LH_Q=2 | AFF_RH_Q=1) agreeableness_f=0.
EXECUTE.

** Agreeableness - Male

IF  (AFM_LH_Q=1 | AFM_RH_Q=2) agreeableness_m=1.
EXECUTE.

IF  (AFM_LH_Q=2 | AFM_RH_Q=1) agreeableness_m=0.
EXECUTE.

** Conscientiousness - Female

IF  (CFF_LH_Q=1 | CFF_RH_Q=2) conscientiousness_f=1.
EXECUTE.

IF  (CFF_LH_Q=2 | CFF_RH_Q=1) conscientiousness_f=0.
EXECUTE.

** Conscientiousness - Male

IF  (CFM_LH_Q=1 | CFM_RH_Q=2) conscientiousness_m=1.
EXECUTE.

IF  (CFM_LH_Q=2 | CFM_RH_Q=1) conscientiousness_m=0.
EXECUTE.

** Extraversion - Female

IF  (EFF_LF_Q=1 | EFF_RH_Q=2) extraversion_f=1.
EXECUTE.

IF  (EFF_LF_Q=2 | EFF_RH_Q=1) extraversion_f=0.
EXECUTE.

** Extraversion - Male

IF  (EFM_LH_Q=1 | EFM_RH_Q=2) extraversion_m=1.
EXECUTE.

IF  (EFM_LH_Q=2 | EFM_RH_Q=1) extraversion_m=0.
EXECUTE.

** Neuroticism - Female

IF  (NFF_LH_Q=1 | NFF_RH_Q=2) neuroticism_f=1.
EXECUTE.

IF  (NFF_LH_Q=2 | NFF_RH_Q=1) neuroticism_f=0.
EXECUTE.

** Neuroticism - Male

IF  (NFM_LH_Q=1 | NFM_RH_Q=2) neuroticism_m=1.
EXECUTE.

IF  (NFM_LH_Q=2 | NFM_RH_Q=1) neuroticism_m=0.
EXECUTE.


** Openness - Female

IF  (OFF_LH_Q=1 | OFF_RH_Q=2) openness_f=1.
EXECUTE.

IF  (OFF_LH_Q=2 | OFF_RH_Q=1) openness_f=0.
EXECUTE.

** Openness - Male

IF  (OFM_LH_Q=1 | OFM_RH_Q=2) openness_m=1.
EXECUTE.

IF  (OFM_LH_Q=2 | OFM_RH_Q=1) openness_m=0.
EXECUTE.

** Narcissism - Female

IF  (NDF_LH_Q=1 | NDF_RH_Q=2) narcissism_f=1.
EXECUTE.

IF  (NDF_LH_Q=2 | NDF_RH_Q=1) narcissism_f=0.
EXECUTE.

** Narcissism - Male

IF  (NDM_LH_Q=1 | NDM_RH_Q=2) narcissism_m=1.
EXECUTE.

IF  (NDM_LH_Q=2 | NDM_RH_Q=1) narcissism_m=0.
EXECUTE.

** Psychopathy - Female

IF  (PDF_LH_Q=1 | PDF_RH_Q=2) psychopathy_f=1.
EXECUTE.

IF  (PDF_LH_Q=2 | PDF_RH_Q=1) psychopathy_f=0.
EXECUTE.

** Psychopathy - Male

IF  (PDM_LH_Q=1 | PDM_RH_Q=2) psychopathy_m=1.
EXECUTE.

IF  (PDM_LH_Q=2 | PDM_RH_Q=1) psychopathy_m=0.
EXECUTE.

** Machiavellianism - Female

IF  (MDF_LH_Q=1 | MDF_RH_Q=2) machiavellianism_f=1.
EXECUTE.

IF  (MDF_LH_Q=2 | MDF_RH_Q=1) machiavellianism_f=0.
EXECUTE.

** Machiavellianism - Male

IF  (MDM_LH_Q=1 | MDM_RH_Q=2) machiavellianism_m=1.
EXECUTE.

IF  (MDM_LH_Q=2 | MDM_RH_Q=1) machiavellianism_m=0.
EXECUTE.


** Statistical tests

NPAR TESTS
  /CHISQUARE=agreeableness_f agreeableness_m conscientiousness_f conscientiousness_m extraversion_f 
    extraversion_m neuroticism_f neuroticism_m openness_f openness_m narcissism_f narcissism_m 
    psychopathy_f psychopathy_m machiavellianism_f machiavellianism_m
  /EXPECTED=EQUAL
  /MISSING ANALYSIS.

