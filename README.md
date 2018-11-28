# Tektronix File Converter

This program takes the internal format used by Tektronix TDS3000 and TDS3000B Oscilloscopes and converts them to a CSV representation.
The tests were run on a TDS3034B and the following assumptions about the internal representation are being made:
* Binary encoding (ENCDG BIN)
* Two bytes per sample point (BYT_NR 2)
* 16 bits per sample (BIT_NR 16)
* Big-endian byte order (BYT_OR MSG)
* Signed binary format (BN_FMT RI)
The CSV conversion is printed to standard output.

## Sample Usage
```
chmod +x tektronix_converter.py
./tektronix_converter.py testdata/test.internal > test.output
```
