--
-- ~ann/pd101/joinem.sql
--

-- Demo:
-- cd ~ann/pd101/
-- sqlite3 pd101.db '.read joinem.sql'

--  This script should inner-join some csv files on cdate.

DROP TABLE EEM;
DROP TABLE EFA;
DROP TABLE EWJ;
DROP TABLE FXI;
DROP TABLE GLD;
DROP TABLE IWM;
DROP TABLE MDY;
DROP TABLE TLT;
DROP TABLE XOM;
DROP TABLE gspc;

CREATE TABLE EEM (eemcdate date, eemp float, eemld float, eem4 float, eem5 float, eem6 float, eem7 float);
CREATE TABLE EFA (efacdate date, efap float, efald float, efa4 float, efa5 float, efa6 float, efa7 float);
CREATE TABLE EWJ (ewjcdate date, ewjp float, ewjld float, ewj4 float, ewj5 float, ewj6 float, ewj7 float);
CREATE TABLE FXI (fxicdate date, fxip float, fxild float, fxi4 float, fxi5 float, fxi6 float, fxi7 float);
CREATE TABLE GLD (gldcdate date, gldp float, gldld float, gld4 float, gld5 float, gld6 float, gld7 float);
CREATE TABLE IWM (iwmcdate date, iwmp float, iwmld float, iwm4 float, iwm5 float, iwm6 float, iwm7 float);
CREATE TABLE MDY (mdycdate date, mdyp float, mdyld float, mdy4 float, mdy5 float, mdy6 float, mdy7 float);
CREATE TABLE TLT (tltcdate date, tltp float, tltld float, tlt4 float, tlt5 float, tlt6 float, tlt7 float);
CREATE TABLE XOM (xomcdate date, xomp float, xomld float, xom4 float, xom5 float, xom6 float, xom7 float);
CREATE TABLE GSPC (gspccdate date, gspcp float, gspcld float, gspc4 float, gspc5 float, gspc6 float, gspc7 float);

.separator ","
.import data/EEM3.csv EEM
.import data/EFA3.csv EFA
.import data/EWJ3.csv EWJ
.import data/FXI3.csv FXI
.import data/GLD3.csv GLD
.import data/IWM3.csv IWM
.import data/MDY3.csv MDY
.import data/TLT3.csv TLT
.import data/XOM3.csv XOM
.import data/GSPC3.csv GSPC

DROP TABLE wide1;
CREATE TABLE wide1 AS
SELECT
eemcdate as cdate
,gspcp as cp
,gspcld as pctlead
,strftime('%w',eemcdate) dow
,strftime('%d',eemcdate) dom
,strftime('%m',eemcdate) moy
,eem4,eem5,eem6,eem7
,efa4,efa5,efa6,efa7
,ewj4,ewj5,ewj6,ewj7
,fxi4,fxi5,fxi6,fxi7
,gld4,gld5,gld6,gld7
,iwm4,iwm5,iwm6,iwm7
,mdy4,mdy5,mdy6,mdy7
,tlt4,tlt5,tlt6,tlt7
,xom4,xom5,xom6,xom7
,gspc4,gspc5,gspc6,gspc7
FROM eem,efa,ewj,fxi,gld,iwm,mdy,tlt,xom,gspc
WHERE eemcdate = efacdate
AND   eemcdate = ewjcdate
AND   eemcdate = fxicdate
AND   eemcdate = gldcdate
AND   eemcdate = iwmcdate
AND   eemcdate = mdycdate
AND   eemcdate = tltcdate
AND   eemcdate = xomcdate
AND   eemcdate = gspccdate
;

.header ON
-- .header OFF
.mode   csv
.output data/wide1.csv

SELECT * FROM wide1 ORDER BY cdate DESC;

.quit
