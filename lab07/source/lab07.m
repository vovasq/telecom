function lab07()

%% coding and encoding using hamming code with matlab in-built functions 
disp('------------Hamming code------------');
out = randerr(1,4) + randerr(1,4);
n = 7;                % Code length
k = 4;                % Message length
code = encode (out, n, k, 'hamming/binary');
disp(code);
dcode = decode (code, n, k, 'hamming/binary');
if (dcode == out) 
    disp('Successful decoding:');
    disp(dcode);
    disp(out);
end;

%% coding and encoding using Cyclic code with matlab in-built functions 
disp('------------Cyclic code-------------');
out = randerr(1,4) + randerr(1,4);
n = 7;                % Code length
k = 4;                % Message length
code = encode (out, n, k, 'cyclic/binary');
disp (code);
dcode = decode (code, n, k, 'cyclic/binary');
if (dcode == out) 
    disp('Successful decoding:');
    disp(dcode);
    disp(out); 
end; 

%% coding and encoding using BCH code with matlab in-built functions 
disp('------------BCH code-----------------');
m = 4;
n = 2^m-1; 
k = 5;       
nwords = 10; 
code = gf(randi([0 1],nwords,k));
[~,t] = bchgenpoly(n,k);
enc = bchenc(code,n,k);
noisycode = enc + randerr(nwords,n,1:t);
dcode = bchdec(noisycode,n,k);
code
dcode
if (code == dcode) 
    disp('Successful decoding:');
    dcode
    code
end;

%% coding and encoding using Reed-Solomon code with matlab in-built functions 
disp('----------Reed-Solomon code-----------');
m = 3;           
n = 2^m - 1;    
k = 3;          
msg = gf([2 7 3; 4 0 6; 5 1 1],m);
code = rsenc(msg,n,k);
errors = gf([2 0 0 0 0 0 0; 3 4 0 0 0 0 0; 5 6 7 0 0 0 0],m);
noisycode = code + errors;
[dcode,cnumerr] = rsdec(noisycode,n,k);
cnumerr

end