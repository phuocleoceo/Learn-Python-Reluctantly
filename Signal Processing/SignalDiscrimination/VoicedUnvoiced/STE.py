def STE(khung, DoDaiKhung):
    frameNum, frameWidth = len(khung)


# function[ste, ste_mau] = STE(khung, DoDaiKhung)
#      [frameNum, frameWidth] = size(khung);
#     ste = 0;
#     for i = 1 : frameNum
#         ste(i) = sum(khung(i,:).^2);
#     end

#     ste = ste./max(ste); %chuan hoa
#     ste_mau = 0;
#     for j = 1 : length(ste)
#          l = length(ste_mau);
#          ste_mau(l : l + DoDaiKhung) = ste(j);
#     end
# end
