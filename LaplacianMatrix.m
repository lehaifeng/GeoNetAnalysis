%function [AdjMat,LapMat,E] = Laplace_Subgraph(nodes,connect)
% show OD matrix [E,AdjMat,LapMat,OD]
% Checking ...
tic;
num = length(adj);
labels = 1 : num;
AdjMat = zeros(num,num);
% calculate the adj matrix

AdjMat(find(adj~=0))=1;

% unweighted graph ...
% normalized laplace matrix
D = diag(sum(AdjMat));
Lap = D - adj;
tempD = diag(D);
tempDD=diag(power(tempD,-1/2));
normalL = tempDD*Lap*tempDD;
% eigvalue ...
E = eig(normalL);
E = sort(E);
i = 0;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
for i=1:length(E)
    if E(i)<0 ;
        E(i) = 0;
    end
    if E(i)>2;
        E(i) = 2;
    end
end  
[x,f] = gauss_smooth(E);
plot(x,f,'r.-')
set(gca,'FontWeight','bold');
set(gcf,'color','w');
xlabel('EigValues')
ylabel('Frequency');
toc;
 % end of function ...