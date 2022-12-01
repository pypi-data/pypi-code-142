'''
	This file is part of mediameta Python package.

	Copyright 2022 Dandelion Systems <dandelion.systems at gmail.com>

	mediameta was inspired and partially based on:
	1. exiftool (https://github.com/exiftool/exiftool) by Phil Harvey
	2. exif-heic-js (https://github.com/exif-heic-js/exif-heic-js), Copyright (c) 2019 Jim Liu

	mediameta is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	mediameta is distributed in the hope that it will be useful, but
	WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
	General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with mediameta. If not, see <http://www.gnu.org/licenses/>.
'''

_TiffTags = {
	0x0100: 'ImageWidth',
	0x0101: 'ImageHeight',
	0x0102: 'BitsPerSample',
	0x0103: 'Compression',
	0x0106: 'PhotometricInterpretation',
	0x010E: 'ImageDescription',
	0x010F: 'Make',
	0x0110: 'Model',
	0x0111: 'StripOffsets',
	0x0112: 'Orientation',
	0x0115: 'SamplesPerPixel',
	0x0116: 'RowsPerStrip',
	0x0117: 'StripByteCounts',
	0x011A: 'XResolution',
	0x011B: 'YResolution',
	0x011C: 'PlanarConfiguration',
	0x0128: 'ResolutionUnit',
	0x012D: 'TransferFunction',
	0x0131: 'Software',
	0x0132: 'DateTime',
	0x013B: 'Artist',
	0x013C: 'HostComputer',
	0x013D: 'Predictor',
	0x013E: 'WhitePoint',
	0x013F: 'PrimaryChromaticities',
	0x0152: 'ExtraSamples',
	0x015B: 'JPEGTables',
	0x0201: 'JPEGInterchangeFormat',
	0x0202: 'JPEGInterchangeFormatLength',
	0x0211: 'YCbCrCoefficients',
	0x0212: 'YCbCrSubSampling',
	0x0213: 'YCbCrPositioning',
	0x0214: 'ReferenceBlackWhite',
	0x02BC: 'XMLPacket',
	0x8298: 'Copyright',
	0x83BB: 'IPTCNAA',
	0x8649: 'ImageResources',
	0x8773: 'InterColorProfile',
	0x00FE: 'NewSubfileType',

	0x8769: 'ExifIFDPointer',
	0x8825: 'GPSInfoIFDPointer',
	0xA005: 'InteroperabilityIFDPointer'
}

_ExifTags = {
	0x0001: 'InteroperabilityIndex',
	0x0002: 'InteroperabilityVersion',
	0x1000: 'RelatedImageFileFormat',
	0x1001: 'RelatedImageWidth',
	0x1002: 'RelatedImageLength',

	0x829A: 'ExposureTime',
	0x829D: 'FNumber',
	0x8822: 'ExposureProgram',
	0x8824: 'SpectralSensitivity',
	0x8827: 'ISOSpeedRatings',
	0x8828: 'OECF',
	0x8829: 'Interlace',
	0x882A: 'TimeZoneOffset',
	0x882B: 'SelfTimerMode',
	0x8830: 'SensitivityType',
	0x8831: 'StandardOutputSensitivity',
	0x8832: 'RecommendedExposureIndex',
	0x9000: 'ExifVersion',
	0x9003: 'DateTimeOriginal',
	0x9004: 'DateTimeDigitized',
	0x9010: 'OffsetTime',
	0x9011: 'OffsetTimeOriginal',
	0x9012: 'OffsetTimeDigitized',
	0x9101: 'ComponentsConfiguration',
	0x9102: 'CompressedBitsPerPixel',
	0x9201: 'ShutterSpeedValue',
	0x9202: 'ApertureValue',
	0x9203: 'BrightnessValue',
	0x9204: 'ExposureBiasValue',
	0x9205: 'MaxApertureValue',
	0x9206: 'SubjectDistance',
	0x9207: 'MeteringMode',
	0x9208: 'LightSource',
	0x9209: 'Flash',
	0x920A: 'FocalLength',
	0x9214: 'SubjectArea',
	0x927C: 'MakerNote',
	0x9286: 'UserComment',
	0x9290: 'SubsecTime',
	0x9291: 'SubsecTimeOriginal',
	0x9292: 'SubsecTimeDigitized',

	0x9C9B: 'XPTitle',
	0x9C9C: 'XPComment',
	0x9C9D: 'XPAuthor',
	0x9C9E: 'XPKeywords',
	0x9C9F: 'XPSubject',

	0xA000: 'FlashpixVersion',
	0xA001: 'ColorSpace',
	0xA002: 'PixelXDimension',
	0xA003: 'PixelYDimension',
	0xA004: 'RelatedSoundFile',
	0xA005: 'InteroperabilityIFDPointer',
	0xA20B: 'FlashEnergy',
	0xA20C: 'SpatialFrequencyResponse',
	0xA20E: 'FocalPlaneXResolution',
	0xA20F: 'FocalPlaneYResolution',
	0xA210: 'FocalPlaneResolutionUnit',
	0xA214: 'SubjectLocation',
	0xA215: 'ExposureIndex',
	0xA217: 'SensingMethod',
	0xA300: 'FileSource',
	0xA301: 'SceneType',
	0xA302: 'CFAPattern',
	0xA401: 'CustomRendered',
	0xA402: 'ExposureMode',
	0xA403: 'WhiteBalance',
	0xA404: 'DigitalZoomRatio',
	0xA405: 'FocalLengthIn35mmFilm',
	0xA406: 'SceneCaptureType',
	0xA407: 'GainControl',
	0xA408: 'Contrast',
	0xA409: 'Saturation',
	0xA40A: 'Sharpness',
	0xA40B: 'DeviceSettingDescription',
	0xA40C: 'SubjectDistanceRange',
	0xA420: 'ImageUniqueID',
	0xA430: 'CameraOwnerName',
	0xA431: 'BodySerialNumber',
	0xA432: 'LensSpecification',
	0xA433: 'LensMake',
	0xA434: 'LensModel',
	0xA435: 'LensSerialNumber',
	0xA500: 'Gamma'
}

_GPSTags = {
	0x0000: 'GPSVersionID',
	0x0001: 'GPSLatitudeRef',
	0x0002: 'GPSLatitude',
	0x0003: 'GPSLongitudeRef',
	0x0004: 'GPSLongitude',
	0x0005: 'GPSAltitudeRef',
	0x0006: 'GPSAltitude',
	0x0007: 'GPSTimeStamp',
	0x0008: 'GPSSatellites',
	0x0009: 'GPSStatus',
	0x000A: 'GPSMeasureMode',
	0x000B: 'GPSDOP',
	0x000C: 'GPSSpeedRef',
	0x000D: 'GPSSpeed',
	0x000E: 'GPSTrackRef',
	0x000F: 'GPSTrack',
	0x0010: 'GPSImgDirectionRef',
	0x0011: 'GPSImgDirection',
	0x0012: 'GPSMapDatum',
	0x0013: 'GPSDestLatitudeRef',
	0x0014: 'GPSDestLatitude',
	0x0015: 'GPSDestLongitudeRef',
	0x0016: 'GPSDestLongitude',
	0x0017: 'GPSDestBearingRef',
	0x0018: 'GPSDestBearing',
	0x0019: 'GPSDestDistanceRef',
	0x001A: 'GPSDestDistance',
	0x001B: 'GPSProcessingMethod',
	0x001C: 'GPSAreaInformation',
	0x001D: 'GPSDateStamp',
	0x001E: 'GPSDifferential',
	0x001F: 'GPSHPositioningError'
}

