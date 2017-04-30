function lab05()

clear;
clc;
close all;

work_path = 'C:\Users\Vovas\YandexDisk\3_course\telecom\labs\lab05\pictures\';

    function plot_spec(s, Fs, t_len, spec_title, png_name)
        n = 2^nextpow2(t_len);
        f = Fs * (0:(n/2))/n;
        spec = fft(s, n);
        spec_fig = figure;
        plot(f, abs(spec(1:n/2+1)))
        title(spec_title);
        xlim([0 100])
        xlabel('frequency')
        ylabel('amplitude')
        saveas(spec_fig, [work_path png_name], 'png');
    end

Fd = 500;
t = 0: 1/Fd: 1;
omega = 3; % modulating signsl
omega0 = 15 ; % carrier
s = cos(omega * 2 * pi * t);
plot_spec(s, Fd, length(t), 'Original signal', '001_origin_spec.png');

% phase modulation
phasedev = 0.1 * pi;
phm_s = pmmod(s,omega0,Fd,phasedev);

plot_spec(phm_s, Fd, length(t), 'Modulated signal', '002_mod_spec.png');

dephm_s = pmdemod(phm_s,omega0,Fd,phasedev);

fig = figure; 
plot(t,s)
title('Original signal')
xlabel('time')
ylabel('amplitude')
saveas(fig, [work_path '003_origin_sig.png'], 'png');

figure; 
plot(t, dephm_s);
title('Recovered signal');
xlabel('time')
ylabel('amplitude')
saveas(fig, [work_path '004_recovered'], 'png');
plot_spec(dephm_s, Fd, length(t), 'DEModulated signal', '005_demod_spec.png');


% freq modulation
freqdev = 0.1 * pi;
fm_s = fmmod(s,omega0,Fd,freqdev);
defm_s = fmdemod(fm_s,omega0,Fd,freqdev);
fig = figure; 
plot(t, fm_s);
title('Modulated signal');
xlabel('time')
ylabel('amplitude')
saveas(fig, [work_path '006_mod_sig.png'], 'png');
plot_spec(defm_s, Fd, length(t), 'DEModulated signal', '007_demod_spec.png');

figure;
plot(t,defm_s, 'b-', t,s, 'g+');

end
