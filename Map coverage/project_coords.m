function [coords2] = project_coords(coords)
%PROJECT_COORDS Project coords to the plane by SVD
coords = coords';
n = size(coords,1);
c = mean(coords);
for j=1:n
    coords(j,:) = coords(j,:) - c;
end
s = svd(coords);
[U,S,V] = svd(coords);
S(3,3) = 0;
coords2 = (U*S);
coords2 = coords2(:,1:2);
coords2 = coords2';
end

