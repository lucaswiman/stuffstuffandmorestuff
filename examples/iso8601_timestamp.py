"""
Parsimonious grammar for the ISO 8601 timestamp format based on the ABNF
grammar from section 5.6 of RFC 3339: https://www.ietf.org/rfc/rfc3339.txt
The original ABNF grammar is here:

    date-fullyear   = 4DIGIT
    date-month      = 2DIGIT  ; 01-12
    date-mday       = 2DIGIT  ; 01-28, 01-29, 01-30, 01-31 based on
                              ; month/year
    time-hour       = 2DIGIT  ; 00-23
    time-minute     = 2DIGIT  ; 00-59
    time-second     = 2DIGIT  ; 00-58, 00-59, 00-60 based on leap second
                              ; rules
    time-secfrac    = "." 1*DIGIT
    time-numoffset  = ("+" / "-") time-hour ":" time-minute
    time-offset     = "Z" / time-numoffset

    partial-time    = time-hour ":" time-minute ":" time-second
                      [time-secfrac]
    full-date       = date-fullyear "-" date-month "-" date-mday
    full-time       = partial-time time-offset

    date-time       = full-date "T" full-time
"""

from parsimonious.grammar import Grammar

ISO8601_RAW_GRAMMAR = """
    date-fullyear   = 4DIGIT
    date-month      = 2DIGIT  ; 01-12
    date-mday       = 2DIGIT  ; 01-28, 01-29, 01-30, 01-31 based on
                              ; month/year
    time-hour       = 2DIGIT  ; 00-23
    time-minute     = 2DIGIT  ; 00-59
    time-second     = 2DIGIT  ; 00-58, 00-59, 00-60 based on leap second
                              ; rules
    time-secfrac    = "." 1*DIGIT
    time-numoffset  = ("+" / "-") time-hour ":" time-minute
    time-offset     = "Z" / time-numoffset

    partial-time    = time-hour ":" time-minute ":" time-second
                      [time-secfrac]
    full-date       = date-fullyear "-" date-month "-" date-mday
    full-time       = partial-time time-offset

    date-time       = full-date "T" full-time
"""

ISO8601 = Grammar(ISO8601_RAW_GRAMMAR)
