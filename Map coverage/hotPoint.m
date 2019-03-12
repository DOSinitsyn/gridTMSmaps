function [ c ] = hotPoints( coords, uV )
%HOTPOINTS Returns coordinates of the stimuli with the highest MEP.
c=coords(:,uV==max(uV));
c = c(:,1);
end

