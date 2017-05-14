function lab07()

close all;
clc;
work_path = 'C:\Users\Vovas\YandexDisk\3_course\telecom\labs\lab07\pictures\';


%% hamming code by encode
n = 15;                % Code length
k = 11;                % Message length
data = randi([0 1],k,1);
d1 = data'
encData = encode(data,n,k,'hamming/binary')
encData = encData .* randerr(15,1,[0 1]); 
decData = decode(encData,n,k,'hamming/binary')'
numerr = biterr(data,decData')  

%% hamming code by parity-check matrix and generation matrix
m = 5;       % param for codeword length 
k = 4;      % Message length
% pc_matrix and gen_matrix - parity-check matrix and generation matrix
% n - codeword length and k - message length
% for m = 2 : 8
%     [check_matrix, gen_matrix, n, k] = hammgen(m);
%     synd_matrix = syndtable(check_matrix);
%     data = randi([0 1],k,1);
%     size(gen_matrix)
%     size(data)
%     % size(check_matrix)
%     % data
%     encData_1 = data' * gen_matrix;
%     size(encData_1)
%     dec_Data_1 = encData_1 * check_matrix' 
%     size(dec_Data_1)    
% end

%% 




end

