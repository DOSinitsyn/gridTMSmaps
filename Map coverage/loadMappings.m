function [maps] = loadMappings(file)
%LOADMAPPINGS Load mappings file 
%   Load mappings from csv file with format (session_id;x;y;z;MEP_amplitude)
raw = load(file);
maps = cell(0);
for j = 1:size(raw,1)
     row = raw(j,:);
     ind = row(1);
     if size(maps,2)<ind
         maps{ind}=row(2:5);
         continue
     end
     maps{ind} = [maps{ind}; row(2:5)];
end
end

