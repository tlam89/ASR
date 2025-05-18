import { useState } from "react";

interface Image {
    imagePath: string;
    labelPath: string;
    diagnosis: string;
    gender: string;
    age: number;
}

interface LeftSidebarProps {
    onImageSelect: (imagePath:string) => void;
}

const LeftSidebar = ({onImageSelect}: LeftSidebarProps) => {
    const [images, setImages] = useState<Image[]>([]);
    const [selectedLesion, setSelectedLesion] = useState("");
    const options: string[] = [
        "Aortic enlargement",
        "Atelectasis",
        "Calcification",
        "Cardiomegaly",
        "Consolidation",
        "ILD",
        "Infiltration",
        "Lung Opacity",
        "Nodule",
        "Other lesion",
        "Pleural Effusion",
        "Pleural thickening",
        "Pneumothorax",
        "Pulmonary fibrosis"
    ];

    const handleDropdownChange: (event: React.ChangeEvent<HTMLSelectElement>) => Promise<void> = async (event) => {
        setSelectedLesion(event.target.value);
        try {
          const formData = new FormData();
          formData.append("classname", event.target.value) 
          const response = await fetch("http://localhost:8002/evaluation/images", {
            method: "POST",
            body: formData,
          });
          const data = await response.json();
          setImages(Object.values(data.images));
    
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
        } catch (error) {
          console.error("Error clipping image:", error);
        }
      };
    
      const handleImageSelection: (sample: Image) => Promise<void> = async (sample) => {
        onImageSelect(sample.imagePath);
        try {
          const formData = new FormData();
          formData.append('file', sample.imagePath);
          const response = await fetch("http://localhost:8000/evaluation/uploading_image", {
            method: 'PUT',
            body: formData,
          });
          if (!response) return;
        } catch (error) {
          console.error('Error uploading image:', error);
        }
      };

    


    return (<div className="p-4 bg-black-900 text-white">
    <div style={{marginTop: '5px', marginBottom: '5px', backgroundColor:"black"}} className="mt-4 flex flex-col gap-2">
      <label>
        Choose an option:
        <select value={selectedLesion} onChange={handleDropdownChange}>
          <option value="">--Select--</option>
          {options.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>   
    </div>

    <div style={{ maxHeight: "80vh", maxWidth: "100%", overflowY: "auto", border: "1px solidrgb(0, 0, 0)", borderRadius: "8px" }} className="no-scrollbar">
      <table style={{maxWidth:"100%"}} className="bg-black">
        <thead>
          <tr className="bg-gray-900">
            <th className="py-2 px-4 border-b border-gray-600 text-white">Image</th>
            {/* <th className="py-2 px-4 border-b border-gray-600 text-white">Case ID</th> */}
            <th className="py-2 px-4 border-b border-gray-600 text-white">Gender</th>
            <th className="py-2 px-4 border-b border-gray-600 text-white">Age</th>
            {/* <th className="py-2 px-4 border-b border-gray-600 text-white">Diagnosis</th> */}
            <th className="py-2 px-4 border-b border-gray-600 text-white">Precision</th>
          </tr>
        </thead>
        <tbody>
          {images.map((image, index) => (
            <tr key={index} className="border-b border-gray-700 bg-black hover:bg-gray-800">
              <td className="py-2 px-4">
                <button
                  key={index}
                  onClick={() => handleImageSelection(image)}
                  className="bg-black w-[96px] h-[96px] flex justify-center items-center rounded-xl shrink-0 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-orange-500"
                  style={{backgroundColor: 'darkgray', borderRadius: '2px'}}
                >
                  <img
                    src={image.labelPath}
                    width={96} 
                    height={96}  
                    alt={image.diagnosis}
                    className="h-24 w-24 object-cover rounded border border-gray-600"
                  />
                </button>

                
              </td>
              {/* <td className="py-2 px-4 text-white">{image.case_id}</td> */}
              <td className="py-2 px-4 text-white">{image.gender}</td>
              <td className="py-2 px-4 text-white">{image.age}</td>
              {/* <td className="py-2 px-4 text-white">{image.diagnosis}</td> */}
              <td className="py-2 px-4 text-white">{0}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>




  </div>
);
};

export default LeftSidebar;