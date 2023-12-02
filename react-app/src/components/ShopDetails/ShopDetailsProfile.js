import React from 'react'

export default function ShopDetailsProfile({shop}) {
    const {name,
        address,
        city,
        state,
        zipCode,
        priceRange,
        businessHours,
        email,
        phoneNumber,
        description,
        coverImageUrl,
        businessImageUrl,
        pickup,
        delivery,
    } = shop

    return (
        <div>
            <img className="shop-cover-img" src={coverImageUrl} alt={`Cover image for ${name}`} />
            <img className="shop-profile-img" src={businessImageUrl} alt={`Profile image for ${name}`} />
            <div>
                <h2>{name}</h2>
                <h3>{address}</h3>
                {/* rating here */}
            </div>
        </div>
    )
    }