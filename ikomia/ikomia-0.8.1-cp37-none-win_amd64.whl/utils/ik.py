ik_binary_to_graphics = "ik_binary_to_graphics"

ik_blob_measurement = "ik_blob_measurement"

ik_blob_cut = "ik_blob_cut"
class ik_blob_cut_param:
    size = "size"

ik_fill_holes = "ik_fill_holes"

ik_graphics_to_binary = "ik_graphics_to_binary"
class ik_graphics_to_binary_param:
    fitToContent = "fitToContent"
    height = "height"
    width = "width"

ik_obj_detection_filter = "ik_obj_detection_filter"
class ik_obj_detection_filter_param:
    confidence = "confidence"
    categories = "categories"

ik_instance_segmentation_filter = "ik_instance_segmentation_filter"
class ik_instance_segmentation_filter_param:
    confidence = "confidence"
    categories = "categories"

ik_semantic_segmentation_filter = "ik_semantic_segmentation_filter"
class ik_semantic_segmentation_filter_param:
    categories = "categories"

ik_plot_merge = "ik_plot_merge"
class ik_plot_merge_param:
    inputCount = "inputCount"

ik_segmentation_rgbhls = "ik_segmentation_rgbhls"
class ik_segmentation_rgbhls_param:
    minB = "minB"
    maxL = "maxL"
    minR = "minR"
    maxB = "maxB"
    minL = "minL"
    maxR = "maxR"
    minG = "minG"
    maxG = "maxG"
    minH = "minH"
    maxH = "maxH"
    minS = "minS"
    maxS = "maxS"

ocv_abs_diff = "ocv_abs_diff"

ocv_add = "ocv_add"
class ocv_add_param:
    dtype = "dtype"

ocv_add_weighted = "ocv_add_weighted"
class ocv_add_weighted_param:
    alpha = "alpha"
    beta = "beta"
    gamma = "gamma"

ocv_compare = "ocv_compare"
class ocv_compare_param:
    operation = "operation"

ocv_convert_to = "ocv_convert_to"
class ocv_convert_to_param:
    alpha = "alpha"
    dtype = "dtype"
    beta = "beta"

ocv_copy_make_border = "ocv_copy_make_border"
class ocv_copy_make_border_param:
    top = "top"
    bottom = "bottom"
    value2 = "value2"
    left = "left"
    right = "right"
    borderType = "borderType"
    value0 = "value0"
    value1 = "value1"
    value3 = "value3"

ocv_count_non_zero = "ocv_count_non_zero"

ocv_crop = "ocv_crop"
class ocv_crop_param:
    left = "left"
    top = "top"
    width = "width"
    height = "height"

ocv_dft = "ocv_dft"
class ocv_dft_param:
    flags = "flags"
    nonZeroRows = "nonZeroRows"

ocv_dft_inverse = "ocv_dft_inverse"
class ocv_dft_inverse_param:
    flags = "flags"
    nonZeroRows = "nonZeroRows"

ocv_divide = "ocv_divide"
class ocv_divide_param:
    scale = "scale"
    dtype = "dtype"

ocv_exp = "ocv_exp"

ocv_extract_channel = "ocv_extract_channel"
class ocv_extract_channel_param:
    index = "index"

ocv_flip = "ocv_flip"
class ocv_flip_param:
    flipCode = "flipCode"

ocv_in_range = "ocv_in_range"
class ocv_in_range_param:
    upper1 = "upper1"
    isLowerScalar = "isLowerScalar"
    lower0 = "lower0"
    lower1 = "lower1"
    lower2 = "lower2"
    isUpperScalar = "isUpperScalar"
    lower3 = "lower3"
    upper0 = "upper0"
    upper2 = "upper2"
    upper3 = "upper3"

ocv_insert_channel = "ocv_insert_channel"
class ocv_insert_channel_param:
    index = "index"

ocv_log = "ocv_log"

ocv_logical_op = "ocv_logical_op"
class ocv_logical_op_param:
    operation = "operation"

ocv_magnitude = "ocv_magnitude"

ocv_max = "ocv_max"
class ocv_max_param:
    isScalar = "isScalar"
    scalar2 = "scalar2"
    scalar0 = "scalar0"
    scalar1 = "scalar1"
    scalar3 = "scalar3"

ocv_merge = "ocv_merge"
class ocv_merge_param:
    inputCount = "inputCount"

ocv_min = "ocv_min"
class ocv_min_param:
    isScalar = "isScalar"
    scalar2 = "scalar2"
    scalar0 = "scalar0"
    scalar1 = "scalar1"
    scalar3 = "scalar3"

ocv_multiply = "ocv_multiply"
class ocv_multiply_param:
    scale = "scale"
    dtype = "dtype"

ocv_negative = "ocv_negative"

ocv_normalize = "ocv_normalize"
class ocv_normalize_param:
    alpha = "alpha"
    dtype = "dtype"
    beta = "beta"
    norm_type = "norm_type"

ocv_psnr = "ocv_psnr"

ocv_rotate = "ocv_rotate"
class ocv_rotate_param:
    rotateCode = "rotateCode"

ocv_split = "ocv_split"
class ocv_split_param:
    outputCount = "outputCount"

ocv_subtract = "ocv_subtract"
class ocv_subtract_param:
    dtype = "dtype"
    value1 = "value1"
    value2 = "value2"
    bUseValue1 = "bUseValue1"
    bUseValue2 = "bUseValue2"

ocv_kmeans = "ocv_kmeans"
class ocv_kmeans_param:
    k = "k"
    termType = "termType"
    termEpsilon = "termEpsilon"
    attempts = "attempts"
    termMaxCount = "termMaxCount"
    flags = "flags"

ocv_dnn_classification = "ocv_dnn_classification"
class ocv_dnn_classification_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    networkType = "networkType"

ocv_dnn_colorization = "ocv_dnn_colorization"
class ocv_dnn_colorization_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"

ocv_dnn_detection = "ocv_dnn_detection"
class ocv_dnn_detection_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    networkType = "networkType"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

ocv_dnn_segmentation = "ocv_dnn_segmentation"
class ocv_dnn_segmentation_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    maskThreshold = "maskThreshold"
    networkType = "networkType"
    confidence = "confidence"

ocv_agast = "ocv_agast"
class ocv_agast_param:
    thresh = "thresh"
    nonmaxsupp = "nonmaxsupp"
    type = "type"

ocv_akaze = "ocv_akaze"
class ocv_akaze_param:
    threshold = "threshold"
    descriptorChannels = "descriptorChannels"
    descriptorType = "descriptorType"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"
    descriptorSize = "descriptorSize"
    nOctaves = "nOctaves"
    diffusivity = "diffusivity"
    nOctaveLayers = "nOctaveLayers"
    bDetect = "bDetect"
    bCompute = "bCompute"

ocv_brisk = "ocv_brisk"
class ocv_brisk_param:
    thresh = "thresh"
    octaves = "octaves"
    bDetect = "bDetect"
    bCompute = "bCompute"
    patternScale = "patternScale"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"

ocv_fast = "ocv_fast"
class ocv_fast_param:
    thresh = "thresh"
    nonmaxsupp = "nonmaxsupp"
    type = "type"

ocv_gftt_detector = "ocv_gftt_detector"
class ocv_gftt_detector_param:
    maxCorners = "maxCorners"
    qualityLevel = "qualityLevel"
    minDistance = "minDistance"
    blockSize = "blockSize"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"
    bUseHarrisDetector = "bUseHarrisDetector"
    bDetect = "bDetect"
    k = "k"
    bCompute = "bCompute"

ocv_kaze = "ocv_kaze"
class ocv_kaze_param:
    threshold = "threshold"
    bExtended = "bExtended"
    bDetect = "bDetect"
    bUpright = "bUpright"
    nOctaves = "nOctaves"
    diffusivity = "diffusivity"
    nOctaveLayers = "nOctaveLayers"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"
    bCompute = "bCompute"

ocv_orb = "ocv_orb"
class ocv_orb_param:
    nlevels = "nlevels"
    nfeatures = "nfeatures"
    scaleFactor = "scaleFactor"
    fastThreshold = "fastThreshold"
    WTA_K = "WTA_K"
    edgeThreshold = "edgeThreshold"
    firstLevel = "firstLevel"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"
    scoreType = "scoreType"
    patchSize = "patchSize"
    bDetect = "bDetect"
    bCompute = "bCompute"

ocv_sift = "ocv_sift"
class ocv_sift_param:
    featuresCount = "featuresCount"
    bUseProvidedKeypoints = "bUseProvidedKeypoints"
    octaveLayersCount = "octaveLayersCount"
    contrastThreshold = "contrastThreshold"
    edgeThreshold = "edgeThreshold"
    sigma = "sigma"
    bDetect = "bDetect"
    bCompute = "bCompute"

ocv_simple_blob_detector = "ocv_simple_blob_detector"
class ocv_simple_blob_detector_param:
    minArea = "minArea"
    minCircularity = "minCircularity"
    minThreshold = "minThreshold"
    minInertiaRatio = "minInertiaRatio"
    maxThreshold = "maxThreshold"
    filterByArea = "filterByArea"
    minDistBetweenBlobs = "minDistBetweenBlobs"
    blobColor = "blobColor"
    maxArea = "maxArea"
    minConvexity = "minConvexity"
    maxCircularity = "maxCircularity"
    filterByConvexity = "filterByConvexity"
    maxConvexity = "maxConvexity"
    filterByCircularity = "filterByCircularity"
    filterByInertia = "filterByInertia"
    maxInertiaRatio = "maxInertiaRatio"

ocv_bf_matcher = "ocv_bf_matcher"
class ocv_bf_matcher_param:
    normType = "normType"
    bCrossCheck = "bCrossCheck"

ocv_flann_based_matcher = "ocv_flann_based_matcher"

ocv_adaptive_threshold = "ocv_adaptive_threshold"
class ocv_adaptive_threshold_param:
    adaptiveMethod = "adaptiveMethod"
    offset = "offset"
    thresholdType = "thresholdType"
    blockSize = "blockSize"

ocv_bilateral_filter = "ocv_bilateral_filter"
class ocv_bilateral_filter_param:
    diameter = "diameter"
    sigmaSpace = "sigmaSpace"
    sigmaColor = "sigmaColor"
    borderType = "borderType"

ocv_box_filter = "ocv_box_filter"
class ocv_box_filter_param:
    ddepth = "ddepth"
    kSizeHeight = "kSizeHeight"
    anchorX = "anchorX"
    bNormalize = "bNormalize"
    kSizeWidth = "kSizeWidth"
    anchorY = "anchorY"
    borderType = "borderType"

ocv_calc_hist = "ocv_calc_hist"
class ocv_calc_hist_param:
    bUniform = "bUniform"
    nBins = "nBins"
    bAccu = "bAccu"
    histSize0 = "histSize0"
    nRanges = "nRanges"
    channels0 = "channels0"
    nChannels = "nChannels"

ocv_canny = "ocv_canny"
class ocv_canny_param:
    threshold1 = "threshold1"
    threshold2 = "threshold2"
    apertureSize = "apertureSize"
    L2gradient = "L2gradient"

ocv_cascade_classifier = "ocv_cascade_classifier"
class ocv_cascade_classifier_param:
    ModelFile1 = "ModelFile1"

ocv_clahe = "ocv_clahe"
class ocv_clahe_param:
    clipLimit = "clipLimit"

ocv_colormap = "ocv_colormap"
class ocv_colormap_param:
    type = "type"

ocv_color_conversion = "ocv_color_conversion"
class ocv_color_conversion_param:
    code = "code"
    dstCn = "dstCn"

ocv_distance_transform = "ocv_distance_transform"
class ocv_distance_transform_param:
    isVoronoi = "isVoronoi"
    type = "type"
    labelType = "labelType"
    maskSize = "maskSize"

ocv_equalize_histogram = "ocv_equalize_histogram"

ocv_gaussian_blur = "ocv_gaussian_blur"
class ocv_gaussian_blur_param:
    sizeX = "sizeX"
    sigmaX = "sigmaX"
    sizeY = "sizeY"
    sigmaY = "sigmaY"
    borderType = "borderType"

ocv_grabcut_segmentation = "ocv_grabcut_segmentation"
class ocv_grabcut_segmentation_param:
    iterationCount = "iterationCount"

ocv_hough_circles = "ocv_hough_circles"
class ocv_hough_circles_param:
    method = "method"
    minDistance = "minDistance"
    param2 = "param2"
    dp = "dp"
    param1 = "param1"
    minRadius = "minRadius"
    maxRadius = "maxRadius"

ocv_hough_lines = "ocv_hough_lines"
class ocv_hough_lines_param:
    stn = "stn"
    probabilistic = "probabilistic"
    threshold = "threshold"
    rho = "rho"
    theta = "theta"
    srn = "srn"
    minTheta = "minTheta"
    maxTheta = "maxTheta"
    minLength = "minLength"
    maxGap = "maxGap"

ocv_laplacian = "ocv_laplacian"
class ocv_laplacian_param:
    ddepth = "ddepth"
    kSize = "kSize"
    scale = "scale"
    delta = "delta"
    borderType = "borderType"

ocv_median_filter = "ocv_median_filter"
class ocv_median_filter_param:
    kSize = "kSize"

ocv_morphology_ex = "ocv_morphology_ex"
class ocv_morphology_ex_param:
    op = "op"
    kernel = "kernel"
    anchorX = "anchorX"
    kernelWidth = "kernelWidth"
    kernelHeight = "kernelHeight"
    borderType = "borderType"
    anchorY = "anchorY"
    iterations = "iterations"
    borderValue = "borderValue"

ocv_resize = "ocv_resize"
class ocv_resize_param:
    isInPixel = "isInPixel"
    newWidth = "newWidth"
    fx = "fx"
    newHeight = "newHeight"
    interpolation = "interpolation"
    fy = "fy"

ocv_rotate_ex = "ocv_rotate_ex"
class ocv_rotate_ex_param:
    angle = "angle"
    scale = "scale"
    centerX = "centerX"
    centerY = "centerY"
    interpolation = "interpolation"

ocv_sobel = "ocv_sobel"
class ocv_sobel_param:
    depth = "depth"
    dx = "dx"
    scale = "scale"
    delta = "delta"
    dy = "dy"
    ksize = "ksize"
    border = "border"

ocv_threshold = "ocv_threshold"
class ocv_threshold_param:
    thresholdType = "thresholdType"
    threshold = "threshold"

ocv_watershed = "ocv_watershed"

ocv_decolor = "ocv_decolor"

ocv_color_change = "ocv_color_change"
class ocv_color_change_param:
    red_mul = "red_mul"
    green_mul = "green_mul"
    blue_mul = "blue_mul"

ocv_denoise_tvl1 = "ocv_denoise_tvl1"
class ocv_denoise_tvl1_param:
    lambda_ = "lambda_"
    niters = "niters"

ocv_detail_enhance_filter = "ocv_detail_enhance_filter"
class ocv_detail_enhance_filter_param:
    sigmaS = "sigmaS"
    sigmaR = "sigmaR"

ocv_edge_preserving_filter = "ocv_edge_preserving_filter"
class ocv_edge_preserving_filter_param:
    flag = "flag"
    sigmaS = "sigmaS"
    sigmaR = "sigmaR"

ocv_non_local_means_filter = "ocv_non_local_means_filter"
class ocv_non_local_means_filter_param:
    h = "h"
    blockSize = "blockSize"
    searchSize = "searchSize"

ocv_non_local_means_multi_filter = "ocv_non_local_means_multi_filter"
class ocv_non_local_means_multi_filter_param:
    h = "h"
    blockSize = "blockSize"
    searchSize = "searchSize"
    temporalSize = "temporalSize"

ocv_illumination_change = "ocv_illumination_change"
class ocv_illumination_change_param:
    alpha = "alpha"
    beta = "beta"

ocv_inpaint = "ocv_inpaint"
class ocv_inpaint_param:
    radius = "radius"
    method = "method"

ocv_pencil_sketch = "ocv_pencil_sketch"
class ocv_pencil_sketch_param:
    sigmaS = "sigmaS"
    shadeFactor = "shadeFactor"
    sigmaR = "sigmaR"

ocv_seamless_cloning = "ocv_seamless_cloning"
class ocv_seamless_cloning_param:
    flags = "flags"

ocv_stylization = "ocv_stylization"
class ocv_stylization_param:
    sigmaS = "sigmaS"
    sigmaR = "sigmaR"

ocv_texture_flattening = "ocv_texture_flattening"
class ocv_texture_flattening_param:
    lowThresh = "lowThresh"
    highThresh = "highThresh"
    kernelSize = "kernelSize"

ocv_tracker_goturn = "ocv_tracker_goturn"

ocv_tracker_kcf = "ocv_tracker_kcf"

ocv_bck_substractor_knn = "ocv_bck_substractor_knn"
class ocv_bck_substractor_knn_param:
    history = "history"
    distanceThreshold = "distanceThreshold"
    isShadowDetect = "isShadowDetect"

ocv_bck_substractor_mog2 = "ocv_bck_substractor_mog2"
class ocv_bck_substractor_mog2_param:
    history = "history"
    varThreshold = "varThreshold"
    isShadowDetect = "isShadowDetect"

ocv_cam_shift = "ocv_cam_shift"
class ocv_cam_shift_param:
    termType = "termType"
    termEpsilon = "termEpsilon"
    termMaxCount = "termMaxCount"

ocv_dis_flow = "ocv_dis_flow"
class ocv_dis_flow_param:
    bUseOCL = "bUseOCL"

ocv_farneback_flow = "ocv_farneback_flow"
class ocv_farneback_flow_param:
    numIters = "numIters"
    fastPyramids = "fastPyramids"
    useOCL = "useOCL"
    winSize = "winSize"
    numLevels = "numLevels"
    polySigma = "polySigma"
    pyrScale = "pyrScale"
    polyN = "polyN"
    flags = "flags"

ocv_mean_shift = "ocv_mean_shift"
class ocv_mean_shift_param:
    termType = "termType"
    termEpsilon = "termEpsilon"
    termMaxCount = "termMaxCount"

ocv_bck_substractor_cnt = "ocv_bck_substractor_cnt"
class ocv_bck_substractor_cnt_param:
    minPixelStability = "minPixelStability"
    maxPixelStability = "maxPixelStability"
    isParallel = "isParallel"
    isUseHistory = "isUseHistory"

ocv_bck_substractor_gmg = "ocv_bck_substractor_gmg"
class ocv_bck_substractor_gmg_param:
    initializationFrames = "initializationFrames"
    threshold = "threshold"

ocv_bck_substractor_gsoc = "ocv_bck_substractor_gsoc"
class ocv_bck_substractor_gsoc_param:
    samples = "samples"
    motionComp = "motionComp"
    replaceRate = "replaceRate"
    alpha = "alpha"
    propagationRate = "propagationRate"
    hitsThreshold = "hitsThreshold"
    beta = "beta"
    blinkingSupressionDecay = "blinkingSupressionDecay"
    blinkingSupressionMultiplier = "blinkingSupressionMultiplier"
    noiseRemovalThresholdFacBG = "noiseRemovalThresholdFacBG"
    noiseRemovalThresholdFacFG = "noiseRemovalThresholdFacFG"

ocv_bck_substractor_lspb = "ocv_bck_substractor_lspb"
class ocv_bck_substractor_lspb_param:
    samples = "samples"
    motionComp = "motionComp"
    TLower = "TLower"
    lsbpRadius = "lsbpRadius"
    TUpper = "TUpper"
    RScale = "RScale"
    TDec = "TDec"
    TInc = "TInc"
    RIncDec = "RIncDec"
    lsbpThreshold = "lsbpThreshold"
    noiseRemovalThresholdFacBG = "noiseRemovalThresholdFacBG"
    noiseRemovalThresholdFacFG = "noiseRemovalThresholdFacFG"
    minCount = "minCount"

ocv_bck_substractor_mog = "ocv_bck_substractor_mog"
class ocv_bck_substractor_mog_param:
    history = "history"
    mixturesCount = "mixturesCount"
    bckRatio = "bckRatio"
    noiseSigma = "noiseSigma"

ocv_adaptive_manifold_filter = "ocv_adaptive_manifold_filter"
class ocv_adaptive_manifold_filter_param:
    sigmaS = "sigmaS"
    numPcaIterations = "numPcaIterations"
    sigmaR = "sigmaR"
    treeHeight = "treeHeight"
    bAdjustOutliers = "bAdjustOutliers"
    bUseRNG = "bUseRNG"

ocv_bilateral_texture_filter = "ocv_bilateral_texture_filter"
class ocv_bilateral_texture_filter_param:
    fr = "fr"
    numIter = "numIter"
    sigmaAlpha = "sigmaAlpha"
    sigmaAvg = "sigmaAvg"

ocv_deriche_gradient_filter = "ocv_deriche_gradient_filter"
class ocv_deriche_gradient_filter_param:
    orientation = "orientation"
    alphaDerive = "alphaDerive"
    alphaMean = "alphaMean"

ocv_dt_filter = "ocv_dt_filter"
class ocv_dt_filter_param:
    sigmaColor = "sigmaColor"
    sigmaSpatial = "sigmaSpatial"
    mode = "mode"
    numIters = "numIters"

ocv_dt_filter_enhance = "ocv_dt_filter_enhance"
class ocv_dt_filter_enhance_param:
    sigmaColor = "sigmaColor"
    sigmaSpatial = "sigmaSpatial"
    numLayer = "numLayer"
    contrastBase = "contrastBase"
    detailsLevel = "detailsLevel"

ocv_dt_filter_stylize = "ocv_dt_filter_stylize"
class ocv_dt_filter_stylize_param:
    sigmaColor = "sigmaColor"
    sigmaSpatial = "sigmaSpatial"
    edgesGamma = "edgesGamma"

ocv_fast_global_smooth_filter = "ocv_fast_global_smooth_filter"
class ocv_fast_global_smooth_filter_param:
    lambda_ = "lambda_"
    lambdaAttenuation = "lambdaAttenuation"
    sigmaColor = "sigmaColor"
    nbIteration = "nbIteration"

ocv_guided_filter = "ocv_guided_filter"

ocv_paillou_gradient_filter = "ocv_paillou_gradient_filter"
class ocv_paillou_gradient_filter_param:
    orientation = "orientation"
    alpha = "alpha"
    omega = "omega"

ocv_joint_bilateral_filter = "ocv_joint_bilateral_filter"
class ocv_joint_bilateral_filter_param:
    diameter = "diameter"
    sigmaSpace = "sigmaSpace"
    sigmaColor = "sigmaColor"
    borderType = "borderType"

ocv_l0_smooth_filter = "ocv_l0_smooth_filter"
class ocv_l0_smooth_filter_param:
    lambda_ = "lambda_"
    kappa = "kappa"

ocv_ridge_filter = "ocv_ridge_filter"
class ocv_ridge_filter_param:
    ddepth = "ddepth"
    out_dtype = "out_dtype"
    dx = "dx"
    scale = "scale"
    delta = "delta"
    dy = "dy"
    ksize = "ksize"
    borderType = "borderType"

ocv_rolling_guidance_filter = "ocv_rolling_guidance_filter"
class ocv_rolling_guidance_filter_param:
    d = "d"
    sigmaColor = "sigmaColor"
    sigmaSpace = "sigmaSpace"
    iter = "iter"
    border = "border"

ocv_fast_line_detector = "ocv_fast_line_detector"
class ocv_fast_line_detector_param:
    lengthThreshold = "lengthThreshold"
    distanceThreshold = "distanceThreshold"
    cannyThreshold1 = "cannyThreshold1"
    cannyThreshold2 = "cannyThreshold2"
    cannyApertureSize = "cannyApertureSize"
    isMerge = "isMerge"

ocv_graph_segmentation = "ocv_graph_segmentation"
class ocv_graph_segmentation_param:
    sigma = "sigma"
    k = "k"
    minSize = "minSize"

ocv_selective_search_segmentation = "ocv_selective_search_segmentation"
class ocv_selective_search_segmentation_param:
    stepK = "stepK"
    sigma = "sigma"
    baseK = "baseK"
    initMethod = "initMethod"
    isDefaultStrategy = "isDefaultStrategy"
    isFillStrategy = "isFillStrategy"
    isColorStrategy = "isColorStrategy"
    colorWeight = "colorWeight"
    fillWeight = "fillWeight"
    isSizeStrategy = "isSizeStrategy"
    sizeWeight = "sizeWeight"
    isTextureStrategy = "isTextureStrategy"
    textureWeight = "textureWeight"
    nbRects = "nbRects"

ocv_superpixel_lsc = "ocv_superpixel_lsc"
class ocv_superpixel_lsc_param:
    regions_size = "regions_size"
    ratio = "ratio"
    num_iterations = "num_iterations"

ocv_superpixel_seeds = "ocv_superpixel_seeds"
class ocv_superpixel_seeds_param:
    num_superpixels = "num_superpixels"
    num_levels = "num_levels"
    prior = "prior"
    double_step = "double_step"
    histogram_bins = "histogram_bins"
    num_iterations = "num_iterations"

ocv_superpixel_slic = "ocv_superpixel_slic"
class ocv_superpixel_slic_param:
    algorithm = "algorithm"
    region_size = "region_size"
    ruler = "ruler"
    num_iterations = "num_iterations"

ocv_structured_edge_detection = "ocv_structured_edge_detection"
class ocv_structured_edge_detection_param:
    algorithm = "algorithm"

ocv_anisotropic_diffusion = "ocv_anisotropic_diffusion"
class ocv_anisotropic_diffusion_param:
    alpha = "alpha"
    K = "K"
    nbIteration = "nbIteration"

ocv_niblack_threshold = "ocv_niblack_threshold"
class ocv_niblack_threshold_param:
    binaryMethod = "binaryMethod"
    thresholdType = "thresholdType"
    blockSize = "blockSize"
    k = "k"

ocv_pei_lin_normalization = "ocv_pei_lin_normalization"
class ocv_pei_lin_normalization_param:
    interpolation = "interpolation"

ocv_thinning = "ocv_thinning"
class ocv_thinning_param:
    type = "type"

ocv_grayworld_wb = "ocv_grayworld_wb"
class ocv_grayworld_wb_param:
    satThreshold = "satThreshold"

ocv_learning_based_wb = "ocv_learning_based_wb"
class ocv_learning_based_wb_param:
    histBinNum = "histBinNum"
    rangeMaxVal = "rangeMaxVal"
    satThreshold = "satThreshold"

ocv_simple_wb = "ocv_simple_wb"
class ocv_simple_wb_param:
    inputMin = "inputMin"
    inputMax = "inputMax"
    outputMin = "outputMin"
    outputMax = "outputMax"
    P = "P"

ocv_xphoto_inpaint = "ocv_xphoto_inpaint"

ocv_deepflow = "ocv_deepflow"
class ocv_deepflow_param:
    bUseOCL = "bUseOCL"

ocv_dual_tvl1_flow = "ocv_dual_tvl1_flow"
class ocv_dual_tvl1_flow_param:
    tau = "tau"
    nscales = "nscales"
    lambda_ = "lambda_"
    theta = "theta"
    warps = "warps"
    epsilon = "epsilon"
    innerIterations = "innerIterations"
    outerIterations = "outerIterations"
    scaleStep = "scaleStep"
    gamma = "gamma"
    medianFiltering = "medianFiltering"
    useInitialFlow = "useInitialFlow"

ocv_pca_flow = "ocv_pca_flow"
class ocv_pca_flow_param:
    width = "width"
    sparseRate = "sparseRate"
    retainedCornersFraction = "retainedCornersFraction"
    height = "height"
    occlusionsThreshold = "occlusionsThreshold"
    dampingFactor = "dampingFactor"
    bUseOCL = "bUseOCL"
    claheClip = "claheClip"

ocv_simple_flow = "ocv_simple_flow"
class ocv_simple_flow_param:
    bUseOCL = "bUseOCL"

ocv_sparse_to_dense_flow = "ocv_sparse_to_dense_flow"
class ocv_sparse_to_dense_flow_param:
    bUseOCL = "bUseOCL"

ocv_retina = "ocv_retina"
class ocv_retina_param:
    useOCL = "useOCL"

ocv_retina_segmentation = "ocv_retina_segmentation"

ocv_motion_saliency_bin_wang = "ocv_motion_saliency_bin_wang"

ocv_objectness_bing = "ocv_objectness_bing"

ocv_static_saliency_fine_grained = "ocv_static_saliency_fine_grained"

ocv_static_saliency_spectral_residual = "ocv_static_saliency_spectral_residual"

ocv_super_resolution_btvl1 = "ocv_super_resolution_btvl1"
class ocv_super_resolution_btvl1_param:
    tau = "tau"
    scale = "scale"
    iterations = "iterations"
    lambda_ = "lambda_"
    blurSigma = "blurSigma"
    alpha = "alpha"
    btvKernelSize = "btvKernelSize"
    blurKernelSize = "blurKernelSize"
    temporalAreaRadius = "temporalAreaRadius"
    opticalFlowType = "opticalFlowType"

ocv_qrcode_detector = "ocv_qrcode_detector"
class ocv_qrcode_detector_param:
    eps_x = "eps_x"
    eps_y = "eps_y"

ocv_ocr_tesseract = "ocv_ocr_tesseract"
class ocv_ocr_tesseract_param:
    oem = "oem"
    psmode = "psmode"

ocv_inpaint_fuzzy = "ocv_inpaint_fuzzy"
class ocv_inpaint_fuzzy_param:
    radius = "radius"
    method = "method"

ocv_hierarchical_feature_selection = "ocv_hierarchical_feature_selection"
class ocv_hierarchical_feature_selection_param:
    minRegionSizeI = "minRegionSizeI"
    segEgbThresholdII = "segEgbThresholdII"
    minRegionSizeII = "minRegionSizeII"
    slicSpixelSize = "slicSpixelSize"
    numSlicIter = "numSlicIter"
    segEgbThresholdI = "segEgbThresholdI"
    spatialWeight = "spatialWeight"

gmic_auto_balance = "gmic_auto_balance"
class gmic_auto_balance_param:
    area = "area"
    smooth = "smooth"
    colorSpace = "colorSpace"
    isBalance = "isBalance"
    isReduceRAM = "isReduceRAM"

gmic_boost_chromaticity = "gmic_boost_chromaticity"
class gmic_boost_chromaticity_param:
    amplitude = "amplitude"
    colorSpace = "colorSpace"

gmic_boost_fade = "gmic_boost_fade"
class gmic_boost_fade_param:
    amplitude = "amplitude"
    colorSpace = "colorSpace"

gmic_color_presets = "gmic_color_presets"
class gmic_color_presets_param:
    hue = "hue"
    category = "category"
    preset = "preset"
    gamma = "gamma"
    brightness = "brightness"
    thumbSize = "thumbSize"
    strenght = "strenght"
    contrast = "contrast"
    saturation = "saturation"
    normalizeColors = "normalizeColors"

gmic_diff_of_gaussians = "gmic_diff_of_gaussians"
class gmic_diff_of_gaussians_param:
    variance1 = "variance1"
    variance2 = "variance2"
    threshold = "threshold"
    isMonochrome = "isMonochrome"
    isNegativeColors = "isNegativeColors"

gmic_distance_transform = "gmic_distance_transform"
class gmic_distance_transform_param:
    value = "value"
    normalization = "normalization"
    metric = "metric"
    modulo = "modulo"

gmic_skeleton = "gmic_skeleton"
class gmic_skeleton_param:
    method = "method"
    smoothness = "smoothness"

gmic_super_pixels = "gmic_super_pixels"
class gmic_super_pixels_param:
    borderColorB = "borderColorB"
    borderColorR = "borderColorR"
    borderOpacity = "borderOpacity"
    size = "size"
    colors = "colors"
    regularity = "regularity"
    iterations = "iterations"
    borderColorG = "borderColorG"
    borderColorA = "borderColorA"

gmic_constrained_sharpen = "gmic_constrained_sharpen"
class gmic_constrained_sharpen_param:
    radius = "radius"
    amount = "amount"
    threshold = "threshold"
    constraintRadius = "constraintRadius"
    valueAction = "valueAction"
    overshoot = "overshoot"
    channel = "channel"

gmic_dynamic_range_increase = "gmic_dynamic_range_increase"
class gmic_dynamic_range_increase_param:
    mapTones = "mapTones"
    isMapTones = "isMapTones"
    recoverShadows = "recoverShadows"
    recoverHighligths = "recoverHighligths"
    enhanceDetails = "enhanceDetails"
    isEnhanceDetails = "isEnhanceDetails"
    detailStrength = "detailStrength"

gmic_magic_details = "gmic_magic_details"
class gmic_magic_details_param:
    amplitude = "amplitude"
    spatialScale = "spatialScale"
    valueScale = "valueScale"
    smoothness = "smoothness"
    edges = "edges"
    channel = "channel"

gmic_sharpen_deblur = "gmic_sharpen_deblur"
class gmic_sharpen_deblur_param:
    radius = "radius"
    iteration = "iteration"
    channel = "channel"
    timeStep = "timeStep"
    smoothness = "smoothness"
    regularization = "regularization"

gmic_sharpen_gradient = "gmic_sharpen_gradient"
class gmic_sharpen_gradient_param:
    amount = "amount"
    scale = "scale"
    values = "values"

gmic_sharpen_richardson_lucy = "gmic_sharpen_richardson_lucy"
class gmic_sharpen_richardson_lucy_param:
    sigma = "sigma"
    iteration = "iteration"
    blur = "blur"
    isCut = "isCut"

gmic_sharpen_tones = "gmic_sharpen_tones"
class gmic_sharpen_tones_param:
    amount = "amount"
    centre = "centre"
    values = "values"

gmic_hot_pixels = "gmic_hot_pixels"
class gmic_hot_pixels_param:
    maskSize = "maskSize"
    threshold = "threshold"

gmic_patch_based_inpaint = "gmic_patch_based_inpaint"
class gmic_patch_based_inpaint_param:
    pathSize = "pathSize"
    lookupSize = "lookupSize"
    lookupFactor = "lookupFactor"
    blendSize = "blendSize"
    lookupInc = "lookupInc"
    blendScales = "blendScales"
    blendThreshold = "blendThreshold"
    isBlendOuter = "isBlendOuter"
    blendDecay = "blendDecay"

gmic_red_eye = "gmic_red_eye"
class gmic_red_eye_param:
    threshold = "threshold"
    smoothness = "smoothness"
    attenuation = "attenuation"

infer_face_detector = "infer_face_detector"
class infer_face_detector_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

infer_facemark_lbf = "infer_facemark_lbf"
class infer_facemark_lbf_param:
    displayType = "displayType"

infer_inception_v3 = "infer_inception_v3"
class infer_inception_v3_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"

infer_mask_rcnn = "infer_mask_rcnn"
class infer_mask_rcnn_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    maskThreshold = "maskThreshold"
    confidence = "confidence"

infer_mobilenet_ssd = "infer_mobilenet_ssd"
class infer_mobilenet_ssd_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

infer_text_detector_east = "infer_text_detector_east"
class infer_text_detector_east_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

infer_yolo_v3 = "infer_yolo_v3"
class infer_yolo_v3_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

infer_yolo_v4 = "infer_yolo_v4"
class infer_yolo_v4_param:
    backend = "backend"
    structureFile = "structureFile"
    datasetName = "datasetName"
    target = "target"
    framework = "framework"
    inputSize = "inputSize"
    modelName = "modelName"
    modelFile = "modelFile"
    labelsFile = "labelsFile"
    confidence = "confidence"
    nmsThreshold = "nmsThreshold"

train_yolo = "train_yolo"
class train_yolo_param:
    configPath = "configPath"
    autoConfig = "autoConfig"
    batchSize = "batchSize"
    model = "model"
    epochs = "epochs"
    classes = "classes"
    inputHeight = "inputHeight"
    gpuCount = "gpuCount"
    inputWidth = "inputWidth"
    learningRate = "learningRate"
    momentum = "momentum"
    outputPath = "outputPath"
    splitRatio = "splitRatio"
    subdivision = "subdivision"
    weightDecay = "weightDecay"

video_in_area_object_counting = "video_in_area_object_counting"
class video_in_area_object_counting_param:
    update_frequency = "update_frequency"
    categories = "categories"
    min_visible_period = "min_visible_period"
    patience = "patience"
    velocity = "velocity"
    output_folder = "output_folder"

