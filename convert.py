from _utils import ComputeNormalmap

import argparse, cv2


def main():

    sigma = 15
    intensity = 100
    nameInput = "test_original.png"
    nameOutput = "test_normal.png"
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma",
                        type=int,
                        default=15,
                        help="Gaussian blur sigma value")
    parser.add_argument("--intensity",
                        type=float,
                        default=100.,
                        help="power of reflected amount")
    parser.add_argument("--input",
                        type=str,
                        default="test_image/test_original.png",
                        help="import file image name")
    parser.add_argument("--output",
                        type=str,
                        default="test_image/test_normalmap.png",
                        help="export file image name")
    
    args = parser.parse_args()
    sigma = args.sigma
    intensity = args.intensity
    nameInput = args.input
    nameOutput = args.output
    
    normal_map = ComputeNormalmap(nameInput, sigma, intensity)
    
    cv2.imwrite(nameOutput, normal_map)


if __name__ == "__main__":
    main()