function lab04()

close all;
clc;
work_path = 'C:\Users\Vovas\YandexDisk\3_course\telecom\labs\lab04\pictures\';

function plot_spec(s, Fs, t_len, png_name)
    n = 2 ^ nextpow2(t_len);
    f = Fs * (0:(n/2))/n;
    spec = fft(s, n);
    spec_fig = figure;
    plot(f, abs(spec(1:n/2+1)))
    xlim([0 100])
    grid on;
    xlabel('frequency')
    ylabel('amplitude')
    saveas(spec_fig, [work_path png_name], 'png');
end
function kpd = kpd(m)
    kpd = m* m  / (m * m + 2);   
end

%% task 1, 2, 3, 7 single tone signal modulation, spectrus, kpd
Fd = 1000;
t = -1 : 2 / Fd : 1;
Fs = 1; 
omega_s = 2 * pi * Fs;
% m = 0.75;
% s_m = (1 +  m * cos(omega_s * t));
Fc = 20; % carrier
for i = 0.1 : 0.5: 3
    s_m = (1 +  i * cos(omega_s * t));
    s_am = ammod(s_m,Fc,Fd);
    fig = figure;
    plot(t, s_am);
    title(['M = ' num2str(i)]);
    hold on;
    grid on;
    plot(t, s_m,'r');
    strr = num2str(i);
    strr = [strr(1) strr(3)];
    saveas(fig, [work_path 'sigm' strr '.png'], 'png');
    plot_spec(s_am, Fd, length(t), ['specm' strr '.png']);
    fprintf('m = %g kpd = %g \n', i, kpd(i));
end

%% task4
% The modulated signal has zero initial phase and zero carrier amplitude, 
% so the result is suppressed-carrier modulation
Fd = 1000;
t = -1 : 2 / Fd : 1;
Fs = 1; 
omega_s = 2 * pi * Fs;
Fc = 20; % carrier
m = 0.75;
s_m = m * cos(omega_s * t);
s_am = ammod(s_m, Fc, Fd, 0);
fig = figure;
plot(t, s_am);
title('Suppresed-carrier modulation');
hold on;
grid on;
plot(t, s_m,'r');
saveas(fig, [work_path 'supcar.png'], 'png');
plot_spec(s_am, Fd, length(t), 'specsupcar.png');

%% task 5, 6 single side band modulation and demodulation
Fd = 1000;
t = -1 : 2 / Fd : 1;
Fc = 25; % carrier
Fs = 1; 
omega_s = 2 * pi * Fs;
m = 0.75;
s_m = m * cos(omega_s * t);
s_ssbu = cos(2 * pi * (Fc + Fs)*t); % modulated signal single-side band upper
fig = figure;
plot(t, s_ssbu);
title('Single-sided modulation');
hold on;
grid on;
saveas(fig, [work_path 'singside.png'], 'png');
% plot_spec(s_ssbu, Fd, length(t), 'specsingside.png');
y = s_ssbu .* cos(2* pi * Fc * t);
[b a] = butter(5, Fc/Fd * 2);
z = filtfilt(b,a,y);
fig = figure;
plot(t,z);
hold on;
grid on;
plot(t, s_m,'r');
saveas(fig, [work_path 'singsideres.png'], 'png');

end