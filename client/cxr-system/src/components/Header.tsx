import React from "react";

const Header: React.FC = () => {
  return (
    <section className="col-[1/4] row-[1/2] bg-gray-600 border-b border-black/10 flex items-center px-4">
      <h1 className="text-white text-xl font-bold">Annotation Tool</h1>
    </section>
  );
};

export default Header;