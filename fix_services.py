import os

hw_dir = "proprietary/bin/hw"
keep_prefixes = [
    "vendor.samsung",
    "vendor.samsung_slsi",
    "android.hardware.drm@1.0-service.widevine",
    "gpsd", "macloader", "mfgloader", "rild", "wpa_supplicant"
]

if os.path.exists(hw_dir):
    for f in os.listdir(hw_dir):
        if not any(f.startswith(p) or f == p for p in keep_prefixes):
            print(f"Deleting conflicting AOSP service: {f}")
            os.remove(os.path.join(hw_dir, f))

# Regenerate device-vendor.mk
src = "proprietary"
mk_lines = []
for root, dirs, files in os.walk(src):
    for f in files:
        rel_path = os.path.relpath(os.path.join(root, f), src)
        android_path = f"$(TARGET_COPY_OUT_VENDOR)/{rel_path}"
        mk_lines.append(f"    vendor/samsung/a2corelte/proprietary/{rel_path}:{android_path}:samsung")

with open("device-vendor.mk", "w") as f:
    f.write("# device-vendor.mk\n\nPRODUCT_COPY_FILES += \\\n")
    f.write(" \\\n".join(mk_lines) + "\n")
print("✅ Regenerated device-vendor.mk without AOSP service conflicts!")
