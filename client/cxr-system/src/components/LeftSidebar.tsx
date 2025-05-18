import React, { useState, useEffect } from 'react';
import ImageGallery from "./ImageGallery"



const LeftSideBar: React.FC = () => {
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);
  const [imageElement, setImageElement] = useState<HTMLImageElement | null>(null);
  const [imageSize, setImageSize] = useState({ width: 512, height: 512 });

  useEffect(() => {
    if (uploadedImage) {
      const img = new Image();
      img.src = uploadedImage;
      img.onload = () => {
        setImageSize({ width: 512, height: 512});
        setImageElement(img);
      };
    }
  }, [uploadedImage]);
  return (
    <section className="col-[1/2] row-[1/3] bg-gray-800 border-r border-black/10 p-4 flex flex-col">
      <h2 className="text-white text-lg font-semibold mb-4">Sidebar</h2>
      <ImageGallery onImageSelect={setUploadedImage}/>
    </section>
  );
};

export default LeftSideBar;