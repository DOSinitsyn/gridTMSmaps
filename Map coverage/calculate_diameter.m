%Calculates the number and fraction of stimuli out of different grid values. 
%
%Input file with mappings information: mappings.csv 
%Format: session_id;x;y;z;MEP_amplitude
%
%Output file: fractions.xlsx
%Columns: 
%active_n - number of stimuli with MEP amplitude > 50,
%outer_n - number of stimuli out of nxn grid
%fraction_n - fraction of stimuli out of nxn grid
%
%Step of the grid is 7.63mm
%From 5x5 to 9x9 grids
clear tab

for n=5:9
    step = 7.63;
    width = n*step;
    half = width/2;

    maps = loadMappings('mappings.csv');

    tsize = size(maps,2);
    active = zeros(tsize,1);
    outer = zeros(tsize,1);
    wb = waitbar(0, ['Calculating for ' num2str(n)]);

    for r=1:tsize
        waitbar(r/tsize);

        map = maps{r};
        coords = map(:,1:3)';
        uv = map(:,4);
        coords = project_coords(coords);

        hp = hotPoint(coords,uv);
        for j = 1 : size(coords,2)
            coords(:,j) = coords(:,j)-hp;
        end


        coords = coords(:,uv>50);
        rad = zeros(size(coords,2),1);
        for k = 1:size(coords,2)
            rad(k) = norm(coords(:,k));
        end

        active(r) = size(coords,2);
        outer(r) = sum(rad>half);

    end

    if(~exist('tab'))
        tab = array2table((1:tsize)','VariableNames',{'session_id'});
    end
    s=num2str(n);
    tmp = array2table([active outer outer./active],'VariableNames',{['active_' s],['outer_' s],['frac_' s]});
    tab = [tab tmp];
    close(wb);
end

writetable(tab,'fractions.xlsx');



