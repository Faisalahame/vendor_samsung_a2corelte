import os

src = "proprietary"
mk_lines = []

for root, dirs, files in os.walk(src):
    for f in files:
        rel_path = os.path.relpath(os.path.join(root, f), src)
        android_path = f"$(TARGET_COPY_OUT_VENDOR)/{rel_path}"
        mk_lines.append(f"    vendor/samsung/a2corelte/proprietary/{rel_path}:{android_path}:samsung")

with open("device-vendor.mk", "w") as f:
    f.write("# device-vendor.mk\n\n")
    f.write("PRODUCT_COPY_FILES += \\\n")
    f.write(" \\\n".join(mk_lines) + "\n")

print("✅ Regenerated device-vendor.mk without toybox conflicts!")
