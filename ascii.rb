require "mini_magick"

print "Enter file name: "
filename = gets.chomp

image = MiniMagick::Image.open(filename)
characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

pixels = image.get_pixels
for i in 0..(pixels.length - 1)
    for j in 0..(pixels[i].length - 1)
        rgb = pixels[i][j]
        brightness = (rgb.reduce :+) / 3
        index = (brightness.to_f / 255 * 65).round
        if index == 0
            print " "
        else
            print characters[index]
        end
    end
    print "\n"
end
