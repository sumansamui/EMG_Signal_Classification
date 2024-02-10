%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GetEMGFileNames.m 
% Read the list of raw EMG data file into a cell
%
% Input:list_file_name
% A string specified the name of file which contains the
% raw dat file names.
% The input file name is specified by a string.
% The input need to be a text file.
% The raw data file names can be recorded in multiple lines
% or seperated by space or TAB in one line in the input file.
% Output: EMG_file
% A N-by-1 cell.
% Each entry of the cell is a file name string.
% Eample:
% >aCell = GetEMGFileNames('fname');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function EMG_file=GetEMGFileNames(list_file_name)
FMAX = 500;                      %max number of entries in the listed in the input file
fid = fopen(list_file_name);     %open the text file containing the file names of the database files.
fcount = 0;
EMG_file = cell(FMAX,1);
while(~feof(fid))                %while NOT zero
aString = fgets(fid);            % read each line of text file
j=1;
while(j <= length (aString))
aName = [];
while(isspace(aString(j))|isequal(aString(j),'\n')|isequal(aString(j),'\r'))
j = j+1;
if(j > length (aString)) break;end;
end;
while(j <= length (aString))
aName =[aName aString(j)];
j=j+1;
if( (j > length (aString))|isspace(aString(j))|isequal(aString(j),'\n')|isequal(aString(j),'\r') )
fcount = fcount + 1;
EMG_file{fcount}= aName;
break;
end;
end;
end;
end;
fclose(fid);
EMG_file = EMG_file(1:fcount);