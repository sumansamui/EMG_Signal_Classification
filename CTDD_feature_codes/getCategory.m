%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%           getCategory.m          %
%Get the category of the data file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function category = getCategory(filename)
if(filename(1:9)=='WristFlex')
    category = 1 ;
elseif (filename(1:9)=='WristExte')
    category = 2 ;
elseif (filename(1:9)=='WristPron')
    category = 3 ;
elseif (filename(1:9)=='WristSupi')
    category = 4 ;
elseif (filename(1:9)=='ObjectGri')
    category = 5 ;
elseif (filename(1:9)=='PichGrip_')
    category = 6 ;
elseif (filename(1:9)=='HandOpen_')
    category = 7 ;
elseif (filename(1:9)=='HandRest_')
    category = 8 ;
end;