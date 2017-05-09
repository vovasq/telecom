function lab06()

close all;
clc;
work_path = 'C:\Users\Vovas\YandexDisk\3_course\telecom\labs\lab06\pictures\';
function plot_cons(sig, path, fig_title)
    f = figure;
    plot(sig,'x','markersize',8);
    grid on;
    title(fig_title)
    xlim([-4 4]);
    ylim([-4 4]);
    xlabel('Quadrature');
    ylabel('In-Phase');
    saveas(f, path, 'png');
end

%% BPSK, PSK, OQPSK, genQAM, MSK

%% BPSK
h = modem.pskmod('M', 2);
g = modem.pskdemod('M', 2);
msg = randint(10,1,2)
modSignal = modulate(h,msg);
errSignal = (randerr(1,10, 3) ./ 30)';
modSignal = modSignal + errSignal;
demodSignal = demodulate(g,modSignal);
plot_cons(modSignal, [work_path  'bpsk.png'],'BPSK'); 
 
%% PSK
h = modem.pskmod('M', 8);
g = modem.pskdemod('M', 8);
msg = randint(10,1,8);
modSignal = modulate(h,msg);
errSignal = (randerr(1,10, 3) ./ 30)';
modSignal = modSignal + errSignal;
demodSignal = demodulate(g,modSignal);
plot_cons(modSignal, [work_path  'psk.png'],'PSK');

%% OQPSK 
h = modem.oqpskmod;
g = modem.oqpskdemod;
msg = randint(200,1,4);
modSignal = modulate(h,msg);
errSignal = (randerr(1,400, 100) ./ 30)';
modSignal = modSignal + errSignal;
demodSignal = demodulate(g,modSignal);
plot_cons(modSignal, [work_path  'oqpsk.png'],'OQPSK');
 
%% genQAM
M = 10;
h = modem.genqammod('Constellation', exp(j*2*pi*[0:M-1]/M));
g = modem.genqamdemod('Constellation', exp(j*2*pi*[0:M-1]/M));
msg = randint(10,1,8);
modSignal = modulate(h,msg);
errSignal = (randerr(1,10, 3) ./ 30)';
modSignal = modSignal + errSignal;
demodSignal = demodulate(g,modSignal);
plot_cons(modSignal, [work_path  'genqam.png'],'genQAM');
                                   
%% MSK modulation
h = modem.mskmod('SamplesPerSymbol', 10);
g = modem.mskdemod('SamplesPerSymbol', 10);
msg = randint(10,1,2);
modSignal = modulate(h, msg);
errSignal = (randerr(1,100, 3) ./ 30)';
modSignal = modSignal + errSignal;
demodSignal = demodulate(g, modSignal);
plot_cons(modSignal, [work_path  'msk.png'],'MSK');

end


% BPSK, PSK, OQPSK, genQAM, MSK, MFSK


% h = modem.pskmod('M', 4); % Modulator object
% g = modem.pskdemod('M', 4); % Demodulator object
% msg = randint(10,1,4); % Modulating message
% modSignal = modulate(h,msg); % Modulate signal


% figHandles = get(0,'Children');
% saveas(figHandles, 'C:\Users\Vovas\YandexDisk\3_course\telecom\labs\lab06\fig\fig01.png', 'png');




% M = 16;             % Modulation alphabet size
% phOffset = 0;       % Phase offset
% symMap = 'binary';  % Symbol mapping (either 'binary' or 'gray')
% hMod = comm.PSKModulator(M, phOffset, 'SymbolMapping', symMap);
% constellation(h)



% to perform QPSK modulation and demodulation
% h = modem.pskmod('M', 4); % Modulator object
% g = modem.pskdemod('M', 4); % Demodulator object
% msg = randint(10,1,4); % Modulating message

% modSignal = modulate(h,msg); % Modulate signal
% demodSignal = demodulate(g,modSignal); % Demodulate sig